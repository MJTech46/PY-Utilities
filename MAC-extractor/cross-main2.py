import netifaces

def get_mac_address_using_netifaces():
    mac_addresses = {}
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        mac = addrs.get(netifaces.AF_LINK, [{}])[0].get('addr')
        if mac:
            mac_addresses[interface] = mac
    return mac_addresses

# Example usage
print("MAC Addresses using netifaces:", get_mac_address_using_netifaces())
