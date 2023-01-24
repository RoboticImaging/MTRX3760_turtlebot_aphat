"""
Script to connect to a new network. Enter SSID, password and static ip address.
This will add the network to the list of possible networks to connect to.

Created: 25/11/2022
Author: Ryan Griffiths
"""

network_file = "/home/ubuntu/.mtrx/wifi.yaml"

def main():
    print('---------------')
    ssid = input('Enter SSID: ')
    password = input('Enter Password: ')
    static_ip = input('Static IP Address: ')
    print('---------------')

    network_config = \
        "    wlan0:\n" + \
        "      dhcp4: yes\n" + \
        "      dhcp6: yes\n" + \
        "      addresses: [{}/32]\n".format(static_ip) + \
        "      optional: true\n" + \
        "      access-points:\n" + \
        "        {}:\n".format(ssid) + \
        "          password: {}\n".format(password)

    with open(network_file, "a") as file_object:
        file_object.write(network_config)

    print("Network configured:\n" + network_config + "---------------")

if '__main__':
    main()