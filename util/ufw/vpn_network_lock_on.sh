#!/bin/bash

# LAN
echo "LAN"
ufw allow out to 192.168.1.0/24
ufw allow out to 192.168.56.0/24

# claranet
echo "Claranet"
ufw allow out to 80.168.87.15

# Proton UK
echo "Proton UK"
ips=$(host uk.protonvpn.com | awk {'print $NF'})
for ip in $ips; do ufw allow out to $ip; done

# Proton Netherlands
echo "Proton Netherlands"
ips=$(host nl.protonvpn.com | awk {'print $NF'})
for ip in $ips; do ufw allow out to $ip; done

# AirVPN Europe
echo "AirVPN Europe"
ips=$(host europe.all.vpn.airdns.org | awk {'print $NF'})
for ip in $ips; do ufw allow out to $ip; done

# VPN Traffic
ufw allow out on tun0
ufw allow out on tun1
ufw allow out on vpn0
# Docker traffic
ufw allow out on docker0

# default reject
ufw default reject outgoing
