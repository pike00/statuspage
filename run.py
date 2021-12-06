import datetime

import requests

import json

sites = []


print("Loading sites...", end="")
with open("config.json") as json_data_file:
    data = json.load(json_data_file)

    sites = data.get("sites")

print("Done\n\n")

print("Checking Sites: ")

for site in sites:
    filename = f"logs/{site}_report.log"
    print(f"\t{site}...", end="")
    req = requests.get(sites[site], timeout=10)

    status = ""
    if req.ok:
        print("UP")
        status = "success"
    else:
        print("DOWN")
        status = "failure"

    with open(filename, 'a+') as log_file:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        log_file.writelines(f"{now},{status}")


print(now)



  # if [[ $commit == true ]]
  # then
  #   echo $dateTime, $result >> "logs/${key}_report.log"