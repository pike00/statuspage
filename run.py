import datetime
import requests
import json
import os

sites = []

os.makedirs("logs",exist_ok=True)

print("Loading sites...", end="")
with open("config.json") as json_data_file:
    data = json.load(json_data_file)

    sites = data.get("sites")

print("Done\n\n")

print("Checking Sites: ")

for site in sites:
    name = site['name']
    url = site['url']
    filename = f"logs/{name}_report.log"

    print(f"\t{name}...", end="")
    req = requests.get(url, timeout=10)

    status = ""
    if req.ok:
        print("UP")
        status = "success"
    else:
        print("DOWN")
        status = "failure"

    with open(filename, 'a+') as log_file:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        log_file.writelines(f"{now},{status}\n")

