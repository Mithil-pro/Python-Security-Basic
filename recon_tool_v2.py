# ==========================================================
# Tool     : Security Recon Tool
# Author   : Tanjim Ahmed Mithil
# Version  : 1.0
# Description : Scans a Target IP for common ports and 
#               identifies services
# Legal    : Only use system you own or have written 
#            permission to test
# ==========================================================

import os 
import datetime

# =========================================
# Tool header
# ========================================

print("=" * 60)
print("      Security recon tool v1.0 ")
print("      Author: Tanjim Ahmed Mithil")
print("=" * 60)
print()

# ================================================
# Function : Identify service running on a port
# ================================================

def get_service(port ):

    services = {
        80 : "HTTP",

        443: "HTTPS",

        22 : "SSH",

        21 : "FTP",

        23 : "TELNET",

        3306: "MYSQL",

        8080: "HTTP-Alt",

        53 : "DNS",

        25 : "SMTP",

        110: "POP3"
    }
    if port in services:
        return services[port]
    else:
        return "unknown service"
    
print("Please provide the scan details ")
print()


target_ip = input("Enter a target ip address : ")

try:
    start_port = int(input("Enter start port : "))
    end_port = int(input("Enter end port : "))

    # ==================================================
    # scan ports and identify services
    # =================================================
    print()
    print("Starting scan on " + target_ip + "......")
    print("_" * 60)

    for port in range(start_port , end_port+1):
        service = get_service(port)
        print("port " + str(port) + " : " + service )

    print("_" * 60)

    # ===================================================
    # saving scan result to a report file
    # ==================================================

    curent_time = datetime.datetime.now()
    date_str = str(curent_time.strftime("%Y-%m-%d_%H-%M-%S"))
    report_name = "recon_report_" + date_str + ".txt"

    with open(report_name,"w") as report:
        report.write(f"{'=' * 60}\n")
        report.write(f"Security recoon tool v2 - SCAN REPORT \n")
        report.write(f"{'=' * 60}\n")
        report.write(f"Target IP: {target_ip}\n")
        report.write(f"Start port: {start_port}\n")
        report.write(f"End port: {end_port}\n")
        report.write(f"Scan time: {date_str}\n")
        report.write(f"{'=' * 60}\n\n")


        for port in range(start_port , end_port+1):
            service = get_service(port)
            report.write(f"Port {port} : {service} \n")
        
    print("Scan complete")
    print("Report saved : " + report_name)




except ValueError:
    print("Invalid port number- Enter numbers only")
