import re
from datetime import datetime

# Example pattern: Failed password for invalid user
FAILED_LOGIN_PATTERN = re.compile(
    r'(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*Failed password.*from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
)

def detect_failed_logins(line):
    match = FAILED_LOGIN_PATTERN.search(line)
    if match:
        return {
            "timestamp": match.group("timestamp"),
            "source_ip": match.group("ip"),
            "event": "Failed Login"
        }
    return None
