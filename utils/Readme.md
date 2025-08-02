# Threat Hunting Log Parser

## Overview
A Python tool to parse Linux `auth.log` files and detect brute-force login attempts. It outputs a summary CSV for investigation or reporting.

## Features
- Detects failed SSH logins
- Extracts source IPs and timestamps
- Easy to extend with more patterns

## Folder Structure
threat-hunting-log-parser/
├── sample_logs/ # Contains test logs
├── reports/ # Output CSV reports
├── utils/ # Detection rules and log patterns


## Getting Started

### Prerequisites
- Python 3.x
- pandas

### Install Dependencies
```bash
pip install -r requirements.txt
