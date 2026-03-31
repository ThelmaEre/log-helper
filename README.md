# SOC Log Helper (Python Cybersecurity Project)

## Overview
This SOC Log Helper is a beginner friendly cybersecurity automation tool built with Python to simulate real Security Operations Center (SOC) analyst workflows. I built this to help me understand some of the tasks an SOC analyst does on a daily basis. This project demonstrates how Python can be used to automate log analysis and investigation tasks commonly performed during security monitoring and incident response.

## Features
- This tool reads and parses authentication log files (in csv format)
- Converts UTC timestamps into local time format to make it readable by humans
- Detects suspicious login behavior (It flags multiple failed logins that occur before a successful login attempt)
- Automatically decodes Base64-encoded commands found in logs
- Renames investigation evidence files automatically

## Skills Demonstrated
- Python scripting for cybersecurity
- Log parsing and analysis
- Detection
- Base64 decoding
- Automation of repetitive SOC tasks

## Technologies Used
- Python

## Example Use Case
Security analysts often export logs from SIEM platforms and must manually analyze suspicious activity. This tool automates parts of that workflow, helping analysts quickly identify anomalies and suspicious behavior.

## Future Improvements
- CAB file parsing for forensic collections
- Automated report generation

## Author
**Thelma Eremionkhale**
