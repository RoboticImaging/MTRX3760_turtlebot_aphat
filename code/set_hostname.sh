#!/bin/bash
# /usr/sbin/change_hostname.sh - program to permanently change hostname.  Permissions
# are set so that www-user can `sudo` this specific program.
# This script runs at reboot, detects if the hostname is different and resets the hostname
# based on the MAC address of the WiFi adapter. The script reboots the machine to force this into effect.

# args:
# $1 - new hostname, should be a legal hostname
host_name=$(hostname)
echo $host_name

IFACE=wlan0
read mac_address </sys/class/net/$IFACE/address

mac_name="$(echo $mac_address| cut -d':' -f 3)$(echo $mac_address| cut -d':' -f 4)$(echo $mac_address| cut -d':' -f 5)$(echo $mac_address| cut -d':' -f 6)pi"

if [ "$mac_name" != "$host_name" ]
    then
        sudo hostnamectl set-hostname $mac_name
        sed -i "15s/.*/        $mac_name:/" /home/ubuntu/.mtrx/ap.yaml
        sudo reboot
fi