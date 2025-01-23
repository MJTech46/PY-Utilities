import psutil # install this module first 

def get_real_mac_address():
    # Iterate over all network interfaces
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:  # AF_LINK is for MAC address
                return f"{interface}: {addr.address}"  # Return interface and MAC address
    return "MAC address not found!"

def main():
    mac_address = get_real_mac_address()
    print("MAC Address:", mac_address)
    input("\nPress Enter to exit...")
    exit()

if __name__ == "__main__":
    main()
