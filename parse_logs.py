import os
import re
import pandas as pd
from utils.log_patterns import detect_failed_logins

def parse_auth_log(file_path):
    results = []
    with open(file_path, 'r') as f:
        for line in f:
            result = detect_failed_logins(line)
            if result:
                results.append(result)

    return pd.DataFrame(results)

def main():
    input_file = "sample_logs/linux_auth.log"
    output_file = "reports/example_report.csv"

    if not os.path.exists(input_file):
        print(f"Input log file not found: {input_file}")
        return

    df = parse_auth_log(input_file)
    df.to_csv(output_file, index=False)
    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    main()
