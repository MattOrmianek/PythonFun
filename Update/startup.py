import sys
import subprocess
import json
import os
import time
import threading


class startup:
    def __init__(self, service, currently_choosen):
        super().__init__()
        self.service = service
        self.currently_choosen = currently_choosen
        self.process = None
        self.status = None

    def start_service(self, service, currently_choosen):
        path = str(currently_choosen) + "/" + "services/" + str(service) + "/run.py"
        self.process = subprocess.Popen(["python3", str(path)])
        return self.process

    def start_service_thread(self, service, currently_choosen):
        thread = threading.Thread(
            target=self.start_service,
            args=(
                service,
                currently_choosen,
            ),
        )
        thread.start()
        return thread

    def monitor_service(self, process):
        print("Monitor running... ")
        while self.process.poll() is None:
            time.sleep(1)
        if self.process.returncode == 0:
            print("Service exited")
        else:
            self.status = "Failed"
        return self.process.returncode

    def start_monitor_thread(self, process):
        thread = threading.Thread(target=self.monitor_service, args=(process,))
        thread.start()
        return thread


# Read config file and check which program is updated
with open("config.json", "r") as config:
    settings = json.load(config)


# Check working folder
currently_choosen = settings["config"]["currently_choosen"]

print(f"currently_choosen: {currently_choosen}")
# Change path to all services to currently_choosen one


## List of services
with open("list_of_services.json", "r") as list_of_services:
    services = json.load(list_of_services)["list_of_services"]

for service in services:
    time.sleep(2)
    try:
        proc = startup(service, currently_choosen)
        process = proc.start_service_thread(service, currently_choosen)
        if str(process.split()[0:8]) == "python3: can't open file":
            print("Can't open file")
        time.sleep(5)
        monitor = proc.start_monitor_thread(process)
    except:
        # change to other folder
        if currently_choosen == "Tom":
            folder_to_update = "Jerry"
        if currently_choosen == "Jerry":
            folder_to_update = "Tom"

        for service in services:
            time.sleep(2)
            proc = startup(service, folder_to_update)
            process = proc.start_service_thread(service, folder_to_update)
            time.sleep(5)
            monitor = proc.start_monitor_thread(process)


## If everything is ok go further, otherwise try running once again and send output to main thread
# time.sleep(60)


# If is running: change updated flag to 0 and send info
if proc.status == None:
    config_file = "/root/testing/config.json"  #! change it after tests
    with open(config_file, "r") as file:
        data = json.load(file)

    data["config"]["update_status"] = 0

    with open(config_file, "w") as file:
        json.dump(data, file, indent=4)

# If not: change startup folder to other one, set flag to update_failed and reboot
if proc.status == "Failed":
    config_file = "/root/config.json"
    with open(config_file, "r") as file:
        data = json.load(file)

    if currently_choosen == "Tom":
        folder_to_update = "Jerry"
    if currently_choosen == "Jerry":
        folder_to_update = "Tom"

    data["config"]["update_status"] = "Failed"
    data["config"]["currently_choosen"] = folder_to_update

    with open(config_file, "w") as file:
        json.dump(data, file, indent=4)
    # os.system('reboot')
