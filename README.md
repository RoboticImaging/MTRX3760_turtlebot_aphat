# MTRX3760 AP Hat Code + Documentation
Code for MTRX3760 AP Hat

## Code
The code found in this repo (in the `code` folder) is on each Turtlebot in a hidden `.mtrx` folder found at `/home/ubuntu/`.

This is used in conjunction with the following lines in the Turtlebot crontab to automatically set hostname, change network state using hardware switch and indicate status live using an LED. You can edit the crontab if needed by running `crontab -e`. You can check the following lines are listed by running `crontab -l`.

```bash

@reboot /home/ubuntu/.mtrx/set_hostname.sh &
@reboot python3 /home/ubuntu/.mtrx/change_wifi.py &
@reboot python3 /home/ubuntu/.mtrx/status_LEDs.py &

```

Students will interface with 2 scripts that can reset and add WiFi networks. These are provided in the `home_files` folder and are to be placed at `/home/ubuntu/`. They are also shipped in the content for the `.mtrx` folder as a backup should they ever be deleted.


## MOTD
We also have additional code which spits out the MAC Address for the Turtlebot and provides a brief welcome message to students. This is included in `/etc/update-motd.d/99-mtrx-mac`. If altering or reconfiguring, you will need to ensure you change permissions such that this file is executable (i.e. `chmod +x` it). This is also provided in the motd folder of this repo.

```bash
#!/bin/sh

IFACE=wlan0
read mac_address </sys/class/net/$IFACE/address

echo "$(tput -T xterm setaf 1)Welcome to MTRX @ The University of Sydney$(tput -T xterm sgr0)"
printf "\nThis is a Turtlebot3 Burger. Please report any issues to your tutor at first boot.\n"

echo "Turtlebot3 has MAC Address: $(echo $mac_address)."
```


## PCB Design
All PCB design files, BOM and circuit schematics are provided in the `pcb_design` folder. These were designed and provided by Tony Cimino of ACFR's tech staff.