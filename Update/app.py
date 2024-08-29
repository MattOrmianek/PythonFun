import os
import tarfile
import json
import subprocess
import time


# MOCK
# config_file_path = "/root/config.json"
config_file_path = "/root/testing/config.json"  #! change it after tests

# Open the JSON file and read its contents
with open(config_file_path, "r") as config_file:
    data = json.load(config_file)


# save_path = "/Users/mateuszormianek/Desktop/Programming/PythonFun/Update"
save_path = "/root/testing"  #! change it after tests

name = "update.tgz"  # basic update package name


def update(data: dict, save_path: str, name: str, folder_to_update=None):
    if "url" in data:
        try:
            url = data["url"]
            # check if updated file is downloaded
            name = name_of_downloaded_file = url.split("/")[-1]

            # deleting file with same name as update package for security
            files = os.listdir(save_path)
            for file in files:
                if file == name_of_downloaded_file:
                    args = ["rm", name_of_downloaded_file]
                    output = subprocess.Popen(args)

            location = save_path
            args = ["wget", "-q", location, url]  # remove '-q' parametr for log output
            output = subprocess.Popen(args)

        except Exception as e:
            print(f"Error {e}")

        # unpack downloaded file
        downloaded_file_path = save_path + "/" + name

        time.sleep(1)  # time.sleep for waiting to save downloaded file, don't remove it

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
                args = ["rm", downloaded_file_path]
                output = subprocess.Popen(args)

        except:
            print("Cannot delete downloaded tar package")

        ## if everything ok: check config, remove other folder, change name of downloaded folder
        # config_file = "/root/config.json"
        config_file = "/root/testing/config.json"  #! change it after tests

        try:
            with open(config_file, "r") as file:
                data = json.load(file)
            currently_choosen = data["config"]["currently_choosen"]

            if currently_choosen == "Tom":
                folder_to_update = "Jerry"
            if currently_choosen == "Jerry":
                folder_to_update = "Tom"

            # path_to_working_folder = f"/root/{folder_to_update}"
            path_to_working_folder = (
                f"/root/testing/{folder_to_update}"  #! change it after tests
            )

            # check if folder exists already (if so delete)
            if os.path.exists(path_to_working_folder):
                args = ["rm", "-r", path_to_working_folder]
                output = subprocess.Popen(args)
                time.sleep(0.5)

            extracted_files_folder = save_path + "/" + extracted_files[0]
            os.rename(extracted_files_folder, path_to_working_folder)

        except Exception as e:
            print(f"Error: {e}")

        data["config"]["currently_choosen"] = folder_to_update
        data["config"]["update_status"] = 1

        try:
            with open(config_file, "w") as file:
                json.dump(data, file, indent=4)

            # os.system('reboot')
            return "Everything works"

        except Exception as e:
            print(f"Error: {e}")


update(data, save_path, name)
