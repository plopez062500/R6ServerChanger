import os
from pathlib import Path

available_servers = ["default", "eastus", "centralus", "southcentralus", "westus", "brazilsouth", "northeurope", "westeurope", "southafricanorth", "eastasia", "southeastasia", "australiaeast", "australiasoutheast", "japanwest"]
local_configs_location = os.path.join(Path.home(), "Documents", "My Games", "Rainbow Six - Siege")
onedrive_configs_location = os.path.join(Path.home(), "OneDrive", "Documents", "My Games", "Rainbow Six - Siege")
active_configs_location = local_configs_location


def locate_configs():
    global active_configs_location
    if not os.path.exists(local_configs_location):
        if os.path.exists(onedrive_configs_location):
            active_configs_location = onedrive_configs_location
        else:
            clear_console()
            print("Unable to find configs")
            exit(1)


def clear_console():
    os.system("cls")


def print_options():
    for i in range(len(available_servers)):
        print("[{0}] {1}".format(i, available_servers[i]))


def read_file_as_list(location):
    f = open(location, "r")
    content = f.read().split('\n')
    f.close()
    return content


def write_list_to_file(location, list):
    content = ""
    for line in list:
        content += line + "\n"
    f = open(location, "w")
    f.write(content)
    f.close()


def update_configuration_file(file_location, new_server):
    content = read_file_as_list(file_location)
    for line in content:
        if line.startswith("DataCenterHint"):
            content[content.index(line)] = "DataCenterHint={0}".format(new_server)
            break
    write_list_to_file(file_location, content)


def main():
    locate_configs()
    while True:
        clear_console()
        print_options()
        try:
            server = available_servers[int(input("Select a server: "))]
        except:
            os.system("cls")
            print("Invalid option")
            input("Press enter to continue...")
            continue

        config_directories = [f.path for f in os.scandir(active_configs_location) if f.is_dir()]

        for directory in config_directories:
            file_location = os.path.join(directory, "GameSettings.ini")
            if os.path.exists(file_location):
                update_configuration_file(file_location, server)

        clear_console()
        print("Server change successful!")
        break


main()
