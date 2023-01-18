# 3760_turtlebot_aphat
Code for MTRX3760 AP Hat


This code found in this repo is on each Turtlebot in a hidden ".mtrx" folder.

This is used in conjunction with the following lines in the Turtlebot crontab to automatically set hostname, change network state using hardware switch and indicate status live using an LED. 

```bash

@reboot /home/ubuntu/.mtrx/set_hostname.sh &
@reboot python3 /home/ubuntu/.mtrx/change_wifi.py &
@reboot python3 /home/ubuntu/.mtrx/status_LEDs.py &

```
