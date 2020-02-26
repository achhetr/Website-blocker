import time
import json
from datetime import datetime as dt

# extract host path from app_setting.json

with open("app_setting.json","r") as file:
    app_setting_file = json.load(file)
    
host_path = app_setting_file["operating_system"]["linux_n_mac_os"]
redirect = "127.0.0.1"

blocked_website = app_setting_file["blocking_website"]

while True:
    # 5 minutes
    time.sleep(300)
    
    # working hours 8 am to 6 pm
    if dt.now().hour >= 8 and dt.now().hour <= 18:
        print("akash")