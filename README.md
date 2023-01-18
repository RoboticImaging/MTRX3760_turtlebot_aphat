# 3760_turtlebot_aphat
Code for MTRX3760 AP Hat


This code found in this repo is on each Turtlebot in a hidden ".mtrx" folder.

This is used in conjunction with the following lines in the Turtlebot crontab to automatically set hostname, change network state using hardware switch and indicate status live using an LED. 

```bash

@reboot /home/ubuntu/.mtrx/set_hostname.sh &
@reboot python3 /home/ubuntu/.mtrx/change_wifi.py &
@reboot python3 /home/ubuntu/.mtrx/status_LEDs.py &

```

We also have additional code which spits out the MAC Address for the Turtlebot and provides a brief welcome message to students. This is included in `/etc/update-motd.d/99-mtrx-mac`. If altering or reconfiguring, you will need to ensure you change permissions such that this file is executable (i.e. `chmod +x` it).

```bash
#!/bin/sh

IFACE=wlan0
read mac_address </sys/class/net/$IFACE/address

echo "$(tput -T xterm setaf 1)Welcome to MTRX @ The University of Sydney$(tput -T xterm sgr0)"
printf "\nThis is a Turtlebot3 Burger. Please report any issues to your tutor at first boot.\n"

echo "Turtlebot3 has MAC Address: $(echo $mac_address)."
```
