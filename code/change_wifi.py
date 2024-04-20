"""
This script runs from a CronJob at reboot in an infinite loop, detecting the state of the AP Hat switch.
If the Turtlebot is already in a state, no actions are taken, but should the state change the netplan
used by the turtlebot is updated to a different mode, and re-applied.

Updates to the netplan may take a moment or two to come into effect. Note the status LED is separate
to this script and operates on the actual state of the network at each point in time.

Created: 25/11/2022
Authors: Jack Naylor & Ryan Griffiths
Updated for 2024: Jack Naylor
"""

import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)


def main():
	# Set as an access point initially, fix undefined behaviour if no AP Hat.
	os.system('sudo cp /home/ubuntu/.mtrx/ap.yaml /etc/netplan/turtlebot_netplan.yaml')
	print("Changing to Access Point")
	os.system('sudo netplan apply')
	while True:
		# GPIO.wait_for_edge(button, GPIO.FALLING)
		with open('/etc/netplan/turtlebot_netplan.yaml') as f:
			current_mode = f.readline().strip('\n')
		print(current_mode)

		if GPIO.input(18) == 0:
			if current_mode != "#AccessPoint":
				os.system('sudo cp /home/ubuntu/.mtrx/ap.yaml /etc/netplan/turtlebot_netplan.yaml')
				print("Changing to Access Point")
				os.system('sudo netplan apply')
		else:
			if current_mode != "#Wifi":
				os.system('sudo cp /home/ubuntu/.mtrx/wifi.yaml /etc/netplan/turtlebot_netplan.yaml')
				print("Changing to Wifi")
				os.system('sudo netplan apply')
		time.sleep(5)

	GPIO.cleanup()


if __name__ == "__main__":
	main()
