# Threat Hunting Log Parser

## Overview
A Python-based tool for parsing and analyzing system logs to detect common threats like brute-force attacks and suspicious logins.

## Features
- Supports Windows Event Logs and Linux auth logs
- Detects failed login patterns, time-based anomalies
- Exports summary reports to CSV

## Technologies
- Python
- Regex
- Pandas

## How to Use
1. Clone the repo
2. Run `python parse_logs.py --input sample.log`
3. Check output report in `/reports`

## Sample Output
![sample screenshot or code output]

## Why I Built This
This tool simulates real-world threat detection logic I've used in previous security roles and demonstrates automated log analysis capabilities.
