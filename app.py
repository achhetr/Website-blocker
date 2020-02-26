import json

# extract host path from app_setting.json

with open("app_setting.json","r") as file:
    app_setting_file = json.load(file)
    
host_path = app_setting_file["operating_system"]["linux_n_mac_os"]
