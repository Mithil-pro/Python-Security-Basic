
"""
Tool Name    : Network & File Health Checker
Author       : Tanjim Ahmed 
Version      : 1.0
Date         : July 2026
Description  : Automates health checks for a list of websites by verifying
               both network-level reachability (via ping) and web-service
               availability (via HTTP status codes). Logs results to a
               timestamped report and organizes reports into dated folders.
Legal        : For educational and authorized use only. Only run against
               systems/websites you own or have explicit permission to test.
"""

#step 1

import os 
import subprocess
import requests 
import datetime

websites = ["google.com" , "youtube.com" , "github.com" , "netflix.com" , "amazon.com"]
#step 2

def check_ping(site):
    result = subprocess.run(["ping" , "-n" , "2" , site], capture_output=True, text = True)
    if result.returncode == 0:
        return True
    else:
        return False
#step 3

def check_web(site):
    try:
        response = requests.get(f"https://{site}")
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False
    
#step 4
 
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

#step 7
if not os.path.exists("reports"):
    os.makedirs("reports")

#step 5

health_report = os.path.join("reports" , f"report_{timestamp}.txt")

healthy_count = 0

with open (health_report, "w") as file:

    for site in websites:
        ping_status = check_ping(site)
        web_status = check_web(site)
        print(f"{site} - Ping: {ping_status}, Web: {web_status}")
        file.write(f"{site} - ping: {ping_status}, web: {web_status}\n")
        if ping_status == True and web_status == True:
            healthy_count = healthy_count + 1

    file.write(f"{healthy_count} out of {len(websites)} sites are fully healthy.")