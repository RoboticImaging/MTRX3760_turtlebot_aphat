'''
RESET WIFI

Use this script to reset *all* wifi networks.
This gives a blank slate.

Author: Jack Naylor
'''

import os

source_dir = "/home/ubuntu/.mtrx/"


def main():

	os.system(f"rm {source_dir}wifi.yaml")
	os.system(f"cp {source_dir}blank_wifi.yaml {source_dir}wifi.yaml")

if __name__ == "__main__":
	main()
