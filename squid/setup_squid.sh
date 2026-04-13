#!/bin/bash
sudo apt update
sudo apt install squid -y
sudo cp squid/squid.conf /etc/squid/squid.conf
sudo systemctl restart squid
sudo systemctl enable squid