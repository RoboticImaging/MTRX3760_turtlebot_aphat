"""
STATUS LEDS

Script to set the state of an LED attached to pin 16 on a Raspberry Pi GPIO based on state of network.
Solid if access point, blinking if connected to WiFi or off if not connected.

Created: 25/11/2022
Author: Ryan Griffiths & Jack Naylor
"""


import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)


def main():

    while True:
        network_status = os.popen('nmcli -t -f active,ssid dev wifi').read().strip('\n')
        hostname = os.popen('hostname').read().strip('\n')

        if (network_status == "yes:"+hostname):
            # Solid if an access point
            GPIO.output(16, 1)
        elif ("yes:" in network_status):
            # Blink if connected to a network
            GPIO.output(16,1)
            time.sleep(0.5)
            GPIO.output(16, 0)
        else:
            # Off if otherwise
            GPIO.output(16,0)


        time.sleep(1)

    GPIO.cleanup()


if __name__ == "__main__":
    main()