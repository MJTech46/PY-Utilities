import uuid

def get_mac_address_using_uuid():
    mac = uuid.getnode()
    if (mac >> 40) % 2:  # Check if it's a valid MAC (not a random locally administered one)
        raise ValueError("Could not find a valid MAC address.")
    return ':'.join(f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -1, -8))

# Example usage
print("MAC Address using uuid:", get_mac_address_using_uuid())
