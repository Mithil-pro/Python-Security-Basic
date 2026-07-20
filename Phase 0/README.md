# Python Security Basics: Custom Reconnaissance Tool

## Overview
This repository contains foundational Python scripts developed for cybersecurity automation. The primary project is a Custom Reconnaissance Tool designed to automate targeted port scanning, map active services, and safely generate timestamped forensic artifacts for incident logging.

## Features
* **Automated Port Scanning:** Iterates through user-defined port ranges to identify open pathways.
* **Service Identification:** Maps discovered open ports to their associated protocols.
* **Forensic Reporting:** Automatically generates and saves timestamped `.txt` artifacts for SOC analysis and record-keeping.
* **Error Handling:** Built-in safeguards to handle invalid inputs gracefully without crashing the tool.

## Usage
Run the script via a Python terminal. You will be prompted to enter a target IP address, a starting port, and an ending port.
`python recon_tool_v2.py`

## Disclaimer
Educational purposes only. This tool is designed for authorized testing and learning environments. Only use on systems you own or have explicit written permission to test.