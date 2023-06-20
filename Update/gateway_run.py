import sys
sys.path.insert(0, '../..')

from lib.zmq import ZMQ
from status import Status
from error import Error
from lib.device import Device
import paho.mqtt.client as mqtt
import asyncio
import json
import time
import tarfile
import os
import json
import subprocess

import shutil
#from lib.journalctl_logger import logger as journal_logger

HB_INTERVAL = 60


class GatewayService(ZMQ):

    VPN_CONNECTED = False

    # override
    def __init__(self, config: dict, logger=print):
        super().__init__(config, logger)
        self.config = config

        self.id = os.environ.get('uid')
        self.devices = []

        self.client = mqtt.Client()

        self.status = Status(self.devices)
        self.error = Error(self.devices, self.config['name'])

        self._init_mqtt()
        self._log(self.config['name'])
        self.register("gpio_event", self._gpio_event)
        self.register("can_event", self._can_event)
        self.register("gpio_config_event", self._gpio_config_event)
        self.register("can_config_event", self._can_config_event)
        self.register("network_config_event", self._network_config_event)
        self.register("vpn_connected", self._VPN_connected)
        self.register("vpn_disconnected", self._VPN_disconnected)
        self.register("can_pm_not_found", self._PM_not_found)
        self.register("pm_error", self._PM_error)
        self.register("nmp_warning", self._no_main_power_warning)
        self.register("at_warning", self._anti_theft_active)

    def _init_mqtt(self):

        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.client.on_message = self._on_message

        mqtt_config = {}
        with open('/root/baseboard/services/gateway/config/mqtt_config.json', 'r') as f:
            mqtt_config = json.load(f)

        self.client.username_pw_set(
            mqtt_config['login'],
            mqtt_config['password']
        )
        try:
            #! bez _async 
            self.client.connect(mqtt_config['host'], mqtt_config['port'])

        except ConnectionRefusedError:
            self._log("Connection refused")
            exit(-1)
        self.client.loop_start()

    def _on_connect(self, client, userdata, flags, rc):
        self._log(f'Connected to MQTT with result code {str(rc)}')
        client.subscribe(f'/request/{self.id}')
        client.subscribe(f'/request/pm/{self.id}')
        client.subscribe(f'/request/gpio/{self.id}')
        client.subscribe(f'/request/whitelist/{self.id}')
        client.subscribe(f'/request/status/{self.id}')
        client.subscribe(f'/request/get_network_config/{self.id}')
        client.subscribe(f'/config/network/{self.id}')
        client.subscribe(f'/config/pm/{self.id}')
        client.subscribe(f'/config/gpio/{self.id}')
        client.subscribe(f'/config/factory_soft_reset/{self.id}')
        client.subscribe(f'/reset/errors/{self.id}')
        client.subscribe(f'/config/mqtt_config/{self.id}')
        client.subscribe(f'/config/update/{self.id}')
        client.subscribe('/broadcast')
        client.subscribe(f'/crt/{self.id}')

        frame = {}

        # sending id to receive configuration
        client.publish(f'/init/{self.id}', json.dumps(frame))

        # Request for first gpio state
        self._send('gpio', 'update')
        self._send('can', 'detect_pms')
        if str(rc) == '0':
            return True
        if str(rc) != '0':
            return False

    def _on_disconnect(self, client, userdata, rc):
        if rc != 0:
            self._log(f"Unexpected MQTT disconnection with code {rc}. Auto-reconnect")

    def _on_message(self, client, userdata, msg): # TODO: adjust the parser to new format / check if current one works as well
        values = msg.topic.split("/")  # retrieve topic name without id // TODO: slice better
        data = {}
        try:
            data = json.loads(msg.payload.decode())
        except json.decoder.JSONDecodeError as e:
            # Handle json decode error here
            self._log(f'JSONDecodeError: {e}')
            # If message is incorrect do nothing
            err =  self.error.get_error(21, f'Bad message from server: {e}')
            self.client.publish(f'/maintenance/error/{self.id}', json.dumps(err))
            self.status.error(21)
            return
        # Log minified string
        self._log(f'Received MQTT {values[1]} mesage: {json.dumps(data, separators=(",", ":"))}')

        try:
            self._parse_msg(values[1], data)
        except KeyError as e:
            self._log("Message type unknown.")

    # override
    def _loop(self):
        loop = asyncio.get_event_loop()
        self._create_listeners(loop)
        loop.create_task(self._heartbeat())
        loop.run_forever()
        loop.close()

    # override
    def _handle_zmq_message(self, message):
        pass

    def _parse_msg(self, topic, data):
        if topic == "request":
            if 'type' not in data:
                self._log("No type provided in the message. Sending status")
                self._pub_full_status()
            elif data['type'] == "request":
                if 'gpio' in data:
                    self._send('gpio', 'request',
                               json.dumps(data['gpio']['data']))
                    # Change of gpio state will trigger reply message automatically

                if 'devices' in data:
                    for device in data['devices']:
                        self._send('can', 'request', json.dumps(device))

                # Reply with full status if no body in request
                if not 'gpio' in data and not 'devices' in data:
                    self._pub_full_status()

            elif data['type'] == "status":
                self._log("Received status request")
                self._pub_full_status()

            elif data['type'] == "request_wl":
                self._log("Received WL request")
                self._pub_full_status()

            elif data['type'] == "restart_device":
                os.system('reboot')

            elif data['type'] == "get_network_config":
                self._log("Received network config request")
                #self._get_network_config_event()
                self._send('network', 'config_update')


        elif topic == "config":
            if data['type'] == "network_config":
                if 'wifi' in data:
                    if 'STA' in data['wifi']:
                        self._log("Received STA configuration")
                        self._send('network', 'config_STA',
                                   json.dumps(data['wifi']['STA']))
                    if 'AP' in data['wifi']:
                        self._log("Received AP configuration")
                        self._send('network', 'config_AP',
                                   json.dumps(data['wifi']['AP']))
                if 'ethernet' in data:
                    self._send('network', 'config_ethernet',
                               json.dumps(data['ethernet']))

                # Trigger a reply with the current network configuration
                self._send('network', 'config_update')

            elif data['type'] == "gpio_config":
                if 'gpio' in data:
                    self._log("Received gpio configuration")
                    self._send('gpio', 'config', json.dumps(data['gpio']))
                 # Trigger a reply with the current gpio configuration
                self._send('gpio', 'config_update')

            elif data['type'] == "pm_config":
                if 'pm' in data:
                    self._log("Received Power Modules configuration")
                    self._send('can', 'config', json.dumps(data['pm']))
                 # Trigger a reply with the current power module configuration
                self._send('can', 'config_update')

            elif data['type'] == "update":
                self._log("Updating process started")
                if 'url' in data:

                    name = "update.tgz" #basic update package name
                    save_path = "/root/testing" #! change after tests
                    config_file_path = "/root/testing/config.json" #! change it after tests

                    # Open the JSON file and read its contents
                    with open(config_file_path, "r") as config_file:
                        config = json.load(config_file)

                    try:
                        url = data['url']
                        # check if updated file is downloaded
                        name = name_of_downloaded_file = url.split('/')[-1]

                        # deleting file with same name as update package for security
                        files = os.listdir(save_path)
                        for file in files:
                            if file == name_of_downloaded_file:
                                args = ['rm', name_of_downloaded_file]
                                output = subprocess.Popen(args)

                        location = save_path
                        args = ['wget', '-q' , location, url] # remove '-q' parametr for log output
                        output = subprocess.Popen(args)

                    except Exception as e:
                        print(f"Error {e}")

                    # unpack downloaded file
                    downloaded_file_path = save_path + '/' + name

                    time.sleep(1) # time.sleep for waiting to save downloaded file, don't remove it

                    if not os.path.exists(downloaded_file_path):
                        print("The .tgz file does not exist in the current directory.")
                        exit()

                    try:
                        with tarfile.open(downloaded_file_path, "r:gz") as tar:
                            tar.extractall()
                            extracted_files = tar.getnames()

                    except Exception as e:
                        print(f"Error {e}")

                    # Remove downloaded tar package

                    try:
                        if os.path.exists(downloaded_file_path):
                            args = ['rm', downloaded_file_path]
                            output = subprocess.Popen(args)

                    except:
                        print("Cannot delete downloaded tar package")


                    ## if everything ok: check config, remove other folder, change name of downloaded folder
                    #config_file = "/root/config.json"
                    config_file = "/root/testing/config.json" #! change it after tests

                    try:
                        with open(config_file, "r") as file:
                            config = json.load(file)
                        currently_choosen = config["config"]["currently_choosen"]

                        if currently_choosen == "Tom": folder_to_update = "Jerry"
                        if currently_choosen == "Jerry": folder_to_update = "Tom"

                        #path_to_working_folder = f"/root/{folder_to_update}"
                        path_to_working_folder = f"/root/testing/{folder_to_update}" #! change it after tests

                        #check if folder exists already (if so delete)
                        if os.path.exists(path_to_working_folder):
                            args = ['rm', '-r', path_to_working_folder]
                            output = subprocess.Popen(args)
                            time.sleep(0.5)

                        extracted_files_folder = save_path + '/' + extracted_files[0]
                        os.rename(extracted_files_folder, path_to_working_folder)

                    except Exception as e:
                        print(f'Error: {e}')

                    config["config"]["currently_choosen"] = folder_to_update
                    config["config"]["update_status"] = 1

                    try:
                        with open(config_file, "w") as file:
                            json.dump(config, file, indent=4)

                        #os.system('reboot')
                        return "Everything works"

                    except Exception as e:
                        print(f"Error: {e}")

            elif data['type'] == "mqtt_config":
                self._log("Received MQTT configuration")
                #if 'host' in data and 'port' in data and 'login' in data and 'password' in data:
                test = True
                if test == True:
                    new_host = data['host']
                    new_port = data['port']
                    new_login = data['login']
                    new_password = data['password']
                    frame = {
                        "host": new_host,
                        "port": new_port,
                        "login": new_login,
                        "password": new_password
                    }

                    mqtt_config = None

                    # Saving old settings
                    with open('/root/baseboard/services/gateway/config/mqtt_config.json',   'r') as f:
                        mqtt_config = f.read()
                        f.close()

                    self.client.on_connect = self._on_connect
                    self.client.on_disconnect = self._on_disconnect
                    self.client.on_message = self._on_message
                    self.client.username_pw_set(
                        new_login,
                        new_password
                    )
                    try:
                        self._log("Trying to connect with new settings")
                        if self.client.connect(new_host, new_port) == True:
                            with open('/root/baseboard/services/gateway/config/mqtt_config.json', 'w') as file:
                                json.dump(frame, file, indent = 4)
                        else:
                            raise ConnectionRefusedError
                    except ConnectionRefusedError:
                        self._log("Connection refused, can't connect, backing up to old settings.")
                        with open('/root/baseboard/services/gateway/config/mqtt_config.json', 'w') as f:
                            f.write(mqtt_config)
                            f.close()

                            self.client.on_connect = self._on_connect
                            self.client.on_disconnect = self._on_disconnect
                            self.client.on_message = self._on_message

                            mqtt_config = {}
                            with open('/root/baseboard/services/gateway/config/mqtt_config.json', 'r') as f:
                                mqtt_config = json.load(f)

                            self.client.username_pw_set(
                                mqtt_config['login'],
                                mqtt_config['password']
                            )
                            try:
                                #! bez _async 
                                self.client.connect_async(mqtt_config['host'], mqtt_config['port'])
                            except Exception as e:
                                self._log("Critical error: " + e)

                    self.client.loop_start()
                    # TODO: konfigurowalny connect timeout, mqtt_client._connect_timeout = 1.0 <- float probably
                else: 
                    self._log("Not valid json with new settings")
            
            elif data['type'] == "factory_soft_reset":
                self._log("Factory soft reset in progress")
                list_of_paths = ['/root/baseboard/services/can/config/can_config','/root/baseboard/services/can/config/service_config','/root/baseboard/services/gateway/config/mqtt_config','/root/baseboard/services/gateway/config/service_config','/root/baseboard/services/gpio/config/gpio_config','/root/baseboard/services/gpio/config/service_config','/root/baseboard/services/led/config/service_config','/root/baseboard/services/lte_monitor/config/lte_monitor_config','/root/baseboard/services/lte_monitor/config/service_config','/root/baseboard/services/network/config/service_config','/root/baseboard/services/touch/config/mqtt_config','/root/baseboard/services/touch/config/service_config','/root/baseboard/services/vpn/config/service_config']
                for path in list_of_paths:
                    with open(path + ".factory", 'r') as f:
                        factory_config = f.read()
                        f.close()
                    
                    self._log(factory_config)
                    
                    with open(path + ".json", 'w') as f:
                        f.write(factory_config)
                        f.close()
                self._log("Factory soft reset done, reboot")
                # uncomment after fixing all problems with this function
                #os.system('reboot')

        elif topic == "broadcast":
            # Only status requests and config requests
            if data['type'] == "request":
                status = self.status.get_full_status()
                self.client.publish(
                    f"/maintenance/status/{self.id}", json.dumps(status))
            #is there response message?
            elif data['type'] == "network_config":
                self._send('network', 'config_update')
            elif data['type'] == "gpio_config":
                self._send('gpio', 'config_update')
            elif data['type'] == "pm_config":
                self._send('can', 'config_update')

        elif topic == "init":
            if data['type'] == "test":
                self._send('vpn', 'stop')

        # removing errors from devices         
        elif topic == "reset":
            if data['type'] == 'reset_error':
                self._log('Error reset')
                self.error.delete_device_error()

        elif topic == "crt":
            with open('/root/baseboard/services/vpn/config/cert.ovpn', 'w') as ovpn_file:
                for line in data[f"{self.id}.conf"]:
                    ovpn_file.write("%s\n" % line)
            self._log("Saved new ovpn configuration")
            self._send('vpn', "change_vpn")
            
        else:
            self._log("Got unknown topic.")
            err =  self.error.get_error(17, 'MQTT message topic unknown.')
            self.client.publish(f'/maintenance/error/{self.id}', json.dumps(err))
            self.status.error(17)

    # GPIO state change will trigger replay status message automatically
    def _gpio_event(self, data):
        self._log(f"Received gpio event: {data}")
        data = json.loads(data)
        self.status.set_gpio(data)
        status = self.status.get_gpio_status()
        self.client.publish(
            f'/maintenance/status/{self.id}', json.dumps(status))

    # Config reply message triggered by config_update request to GPIO Service
    def _gpio_config_event(self, data):
        self._log(f"Received gpio config event: {data}")
        data = json.loads(data)
        frame = {
            "type": "gpio_config",
            "timestamp": int(time.time()),
            "gpio": data
        }
        self.client.publish(f'/maintenance/status/{self.id}', json.dumps(frame))
        self._pub_full_status()

    def _can_event(self, data):
        self._log(f"Received can event")# {data}" )
        data = json.loads(data)
        for i in range(0, len(data)):
            data[i] = json.loads(data[i])
        self.devices = data
        self.status.set_devices(data)
        status = self.status.get_full_status()
        self.client.publish(
            f'/maintenance/status/{self.id}', json.dumps(status))

    # Config reply message triggered by config_update request to CAN Service
    def _can_config_event(self, data):
        self._log(f"Received can config event:") #{data}")
        data = json.loads(data)
        frame = {
            "type": "pm_config",
            "timestamp": int(time.time()),
            "pm": data
        }
        self.client.publish(f'/maintenance/status/{self.id}', json.dumps(frame))
        # self._pub_full_status()

    # Config reply message triggered by config_update request to Network Service
    def _network_config_event(self, data):
        self._log(f"Received network event: {data}")
        data = json.loads(data)
        frame = {
            "type": "network_config",
            "timestamp": int(time.time()),
            "wifi": data['wifi'],
            "ethernet": data['ethernet']
        }
        self.client.publish(f'/maintenance/status/{self.id}', json.dumps(frame))
        self._pub_full_status()

     # Get network config message reply for request
    def _get_network_config_event(self):
        self._pub_full_status()

    # Sending no main power warning
    def _no_main_power_warning(self):
        self._log("No main power")
        frame = {
            "type": "warning",
            "timestamp": int(time.time()),
            "details": {
                "code": 999,
                "description": "Main power loss"
            }
        }
        self.client.publish(f"/maintenance/warning/{self.id}", json.dumps(frame))

    # Sending anti theft warning 
    def _anti_theft_active(self):
        self._log("Anti_theft button active")
        frame = {
            "type": "warning",
            "timestamp": int(time.time()),
            "details": {
                "code": 997,
                "description": "Anti-theft button active"
            }
        }
        self.client.publish(f"/maintenance/warning/{self.id}", json.dumps(frame))
      
    def _VPN_connected(self):
        self._log('Connected to VPN')
        self.VPN_CONNECTED = True

    def _VPN_disconnected(self):
        self._log('Disconnected from VPN')
        self.VPN_CONNECTED = False

    def _PM_not_found(self, data):
        data = json.loads(data)
        err =  self.error.get_error(100, f"PM with ID: {data['id']} not found")
        self.client.publish(f'/maintenance/error/{self.id}', json.dumps(err))
        self.status.error(100)

    def _PM_error(self, data):
        self.error.append_device_error(data)
        err = self.error.get_error(1, "PM error")
        self.client.publish(f'/maintenance/error/{self.id}', json.dumps(err))

    # getting full status
    def _pub_full_status(self):
        status = self.status.get_full_status()
        self.client.publish(f'/maintenance/status/{self.id}', json.dumps(status))

    # Cyclic heartbeat frame 
    async def _heartbeat(self):
        await asyncio.sleep(5)
        while True:
        
            device_ids = [pm['id'] for pm in self.devices]
            hb = {
                'type': 'hb',
                'timestamp': int(time.time()),
                'devices': device_ids
            }
            self.client.publish(
                f'/maintenance/heartbeat/{self.id}', json.dumps(hb))
            self._log(f'Sending heartbeat frame')
            await asyncio.sleep(HB_INTERVAL)

if __name__ == '__main__':
    config = {}
    with open("/root/baseboard/services/gateway/config/service_config.json") as file:
        config = json.loads(file.read())
    service = GatewayService(config)
    service.run()
