#!/usr/bin/env python3

import sys
import ipaddress
import subprocess
import json

if len(sys.argv) < 2:
    print("Usage: netscan.py <ADR-range>     (example: 192.168.1.0 - utility assumes /24 or Class C network in IP4 address space.)")
    sys.exit(1)
else:
	ip_address = sys.argv[1]


def extract_network(ip_address):
	try:
		# validate the ip
		ip = ipaddress.ip_address(ip_address)

		# extract the entwork portion
		network = ip.network
		return str(network)
	except ValueError:
		print("Invalid IP address. Valid example 192.168.1.55 - exiting.")
		return None



def scan_network(network):
    network_macs = {'ipaddress':[],'macaddress':[]}
    try:
        # Create an IP network object
        ip_net = ipaddress.ip_network(network)

        # Iterate over each IP address in the network
        for ip in ip_net.hosts():
            ip_address = str(ip)

            # Ping the IP address to check if it is reachable
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip_address], stdout=subprocess.DEVNULL)

            # Check the return code to determine if the IP address is reachable
            if result.returncode == 0:
                  print(ip_address, "is reachable.")
        macaddress = find_mac_address(ip_address)
        if (macaddress != "Failed to find MAC address"):
            network_macs[ip_address] = (ip_address, macaddress)
        else:
            print(ip_address, "is not reachable.")

        file_path = network+'.json'
        with open(file_path, 'w') as json_file:
            json.dump(network_macs, json_file)
    
        print("List of IP and Mac addresses saved as ",file_path)

    except ValueError:
        print("Invalid network address")


def find_mac_address(ip_address):
    try:
        # Execute the arp command to retrieve MAC address information
        arp_output = subprocess.check_output(['arp', '-n', ip_address]).decode()

        # Extract the MAC address from the command output
        mac_address = arp_output.split()[3]

        return mac_address
    except subprocess.CalledProcessError:
        print("Failed to find MAC address")
        return None


scan_network(extract_network(ip_address))
