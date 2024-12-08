import re
import csv
from collections import defaultdict

def analyze_log_entries(log_entries):
    req_count_ip = defaultdict(int)  
    access_count = defaultdict(int)   
    failed_logins = defaultdict(int)   

    for entry in log_entries:
        log_pattern = r'(\S+) - - \[.*\] "(.*?) (.*?) HTTP.*" (\d{3}) .*'
        match = re.match(log_pattern, entry)
        if match:
            ip, method, endpoint, status = match.groups()
            req_count_ip[ip] += 1
            access_count[endpoint] += 1
            if method == "POST" and status == "401":
                failed_logins[ip] += 1
    return req_count_ip, access_count, failed_logins

def print_and_save_analysis(ip_counts, endpoint_counts, failed_logins, csv_path):
    csv_output = []
    print("IP Address, Request Count")
    csv_output.append(["IP Address", "Request Count"])
    for ip, count in ip_counts.items():
        print(f"{ip}, {count}")
        csv_output.append([ip, count])
    print()
    print("Most Accessed Endpoint, Access Count")
    most_accessed = max(endpoint_counts.items(), key=lambda x: x[1])
    print(f"{most_accessed[0]}, {most_accessed[1]}")
    csv_output.append(["Most Accessed Endpoint", "Access Count"])
    csv_output.append([most_accessed[0], most_accessed[1]])
    print()
    print("IP Address, Failed Login Count")
    csv_output.append(["IP Address", "Failed Login Count"])
    for ip, count in failed_logins.items():
        print(f"{ip}, {count}")
        csv_output.append([ip, count])
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_output)
