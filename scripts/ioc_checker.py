import re

LOG_FILE = "/var/log/snort/alert"

patterns = [
    r"ICMP Ping Detected",
    r"HTTP Traffic Detected",
    r"HTTPS Connection Detected"
]

with open(LOG_FILE, "r", errors="ignore") as f:
    data = f.read()

print("=== Indicators of Compromise ===")
for pattern in patterns:
    matches = re.findall(pattern, data)
    print(f"{pattern}: {len(matches)} matches")