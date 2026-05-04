import re
from collections import defaultdict

with open("blacklist.txt", "r") as f:
    blacklist = set(ip.strip() for ip in f.readlines())

with open("logs.txt", "r") as f:
    logs = f.readlines()

failed_attempts = defaultdict(int)
alerts = []

for log in logs:
    ip_match = re.search(r'ip=(\d+\.\d+\.\d+\.\d+)', log)
    status = "FAILED" if "FAILED" in log else "SUCCESS"

    if ip_match:
        ip = ip_match.group(1)

        if status == "FAILED":
            failed_attempts[ip] += 1

        if failed_attempts[ip] >= 3:
            alerts.append(f"⚠️ Brute Force Detected from IP: {ip}")

        if ip in blacklist:
            alerts.append(f"🚫 Blacklisted IP Access: {ip}")

with open("report.txt", "w", encoding="utf-8") as f:
    for alert in set(alerts):
        f.write(alert + "\n")

print("Analysis Complete. Check report.txt")