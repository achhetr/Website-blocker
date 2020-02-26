import time
import json
from datetime import datetime as dt
import os, platform

# extract host path from app_setting.json

with open("app_setting.json","r") as file:
    app_setting_file = json.load(file)

if platform.system() == "Windows":
    host_path = app_setting_file["operating_system"]["win_os"]
else:
    host_path = app_setting_file["operating_system"]["linux_n_mac_os"]

redirect_v4 = "127.0.0.1"
redirect_v6 = "0:0:0:0:0:FFFF:0A00:0117"
 
blocked_website = app_setting_file["blocking_website"]

while True:
    # 5 minutes
    time.sleep(5)
    
    # working hours 8 am to 6 pm
    if dt.now().hour >= 8 and dt.now().hour <= 18:
        print("\n\nWorking Hours\n\n")
        with open(host_path,"r+") as file:
            hosts_content = file.read()

            for website in blocked_website:
                if website in hosts_content:
                    pass
                else:
                    print("Blocking "+ website + " now....")
                    file.write(redirect_v4 + " " + website + "\n")
                    file.write(redirect_v6 + " " + website + "\n")
                    time.sleep(1)


    else:
        print("\n\nNon Working Hours\n\n")
        with open(host_path,"r+") as file:
            content_list = file.readlines()    
            file.seek(0)

            for line in content_list:
                if not any(website in line for website in blocked_website):
                    file.write(line)
                
            file.truncate()

    os.system("sudo dscacheutil -flushcache")