import os
import platform
import re

def get_mac_address_using_os():
    if platform.system() == "Windows":
        command = "ipconfig /all"
    else:
        command = "ifconfig"

    result = os.popen(command).read()
    mac_pattern = r"(([a-fA-F0-9]{2}[-:]){5}[a-fA-F0-9]{2})"
    mac_addresses = re.findall(mac_pattern, result)

    return [mac[0] for mac in mac_addresses]  # Extract the full MAC addresses

# Example usage
print("MAC Addresses using os:", get_mac_address_using_os())
