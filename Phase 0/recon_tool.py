# ====================================================
# Tool   : Security Recon Tool
# Author : Tanjim Ahmed Mithil
# version: 1.0
# Description : Scans a Target IP for common
#                 ports and identifies services
# Legal  : Only use systems you own or 
#          have written permission to test
# ===================================================

import os
import datetime

# ================================
# Display tool header 
#=================================
print("=" * 60)
print( "     SECURITY RECON TOOL v1.0")
print("      Author: TANJIM AHMED MITHIL")
print("=" * 60)
print()

# ===============================================
# Function: identify service running on a port
# ===============================================
def get_service(port ):
    services = {
        80 : "HTTP",

        443: "HTTPS",

        22 : "SSH",

        21 : "FTP",

        23 : "TELNET",

        3306:"MY SQL",

        8080:"HTTP-Alt",

        53  : "DNS",

        25  : "SMTP",

        110 : "POP3"
    }
    if port in services:
        return services[port]
    else:
        return "Unknown Service"
    

print("Please provide scan details:")
print()


target_ip = input("Enter target IP address : ")

try:
    start_port = int(input("Enter start port     : "))
    end_port   = int(input("Enter end port       : "))
    # ============================================
    # Scan ports and identify services
    # ============================================

    print()
    print("Starting scan on " + target_ip + " ....")
    print("_" * 60)

    for port in range(start_port , end_port + 1):
        service = get_service(port)
        print("Port " + str(port) + " : " + service)

    print("_" * 60)

    # =====================================================
    # Save scan result to a report file
    # =====================================================
    now = datetime.datetime.now()
    date_str = str(now.strftime("%Y-%m-%d_%H-%M-%S"))
    report_name = "recon_report_" + date_str + ".txt"


    with open(report_name , "w") as report:
        report.write("=" * 60 + "\n")
        report.write("SECURITY RECON TOOL v1.0 - SCAN REPORT\n")
        report.write("=" * 60 + "\n")
        report.write("Target IP  : " + target_ip + "\n")
        report.write("Start Port : " + str(start_port) + "\n")
        report.write("End Port   : " + str(end_port) + "\n")
        report.write("Scan Time  : " + date_str + "\n")
        report.write("=" * 60 + "\n\n")

        for port in range(start_port , end_port + 1):
            service = get_service(port)
            report.write("Port " + str(port) + " :" + service + "\n")


        report.write("\n" + "=" * 60 + "\n")
        report.write("Scan Complete.\n")

    print("Scan complete. ")
    print("Report saved : " + report_name )







except ValueError:
    print("Invalid port number - please enter numbers only")


    