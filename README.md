# Implementing and Studying Firewall Technologies for Blocking Malicious Traffic
“Implementing and Studying Firewall Technologies for Blocking Malicious Traffic”  Modern networks are increasingly targeted by malicious traffic, including adware, spyware, phishing, and unauthorized access attempts. Traditional firewalls, with their limited rule-based filtering, often fail to detect and block these sophisticated threats.


This project demonstrates a layered network defense using:
- Snort (IDS/IPS)
- Squid Proxy
- OpenVPN
- Wireshark

## Features
- Detects malicious traffic
- Blocks adware domains
- Secure VPN tunnel
- IOC analysis
- Packet monitoring

## Setup
```
chmod +x snort/run_snort.sh
chmod +x squid/setup_squid.sh
chmod +x openvpn/setup_openvpn.sh
./snort/run_snort.sh
```
# 2) .gitignore

```gitignore
*.log
*.pcap
__pycache__/
*.pyc
*.ovpn
logs/*
!logs/.gitkeep



