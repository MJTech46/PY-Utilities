import psutil
import random

class MacUtils:
    @staticmethod
    def get_real_mac_addresses():
        """
        Collect MAC addresses from all available network interfaces.

        Returns:
            dict: A dictionary where keys are interface names and values are MAC addresses.
        """
        mac_addresses = {}
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == psutil.AF_LINK:  # AF_LINK is for MAC address
                    mac_addresses[interface] = addr.address
        return mac_addresses

    @staticmethod
    def get_random_mac_address():
        """
        Generate a random MAC address.

        Returns:
            str: A randomly generated MAC address in the format XX:XX:XX:XX:XX:XX.
        """
        return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

    @staticmethod
    def format_mac_address(mac_address, delimiter=':'):
        """
        Format a MAC address string by adding a custom delimiter.

        Args:
            mac_address (str): A MAC address string without delimiters (e.g., "AABBCCDDEEFF").
            delimiter (str): The delimiter to use (default is ':').

        Returns:
            str: A formatted MAC address string.
        """
        if len(mac_address) != 12:
            raise ValueError("MAC address must be 12 characters long without delimiters.")
        return delimiter.join(mac_address[i:i+2] for i in range(0, 12, 2))

# Example usage
if __name__ == "__main__":
    mac_utils = MacUtils()

    # Collect real MAC addresses
    real_macs = mac_utils.get_real_mac_addresses()
    print("Real MAC Addresses:")
    for interface, mac in real_macs.items():
        print(f"{interface}: {mac}")

    # Generate a random MAC address
    random_mac = mac_utils.get_random_mac_address()
    print("\nRandom MAC Address:", random_mac)

    # Format a MAC address
    try:
        formatted_mac = mac_utils.format_mac_address("AABBCCDDEEFF", '-')
        print("\nFormatted MAC Address:", formatted_mac)
    except ValueError as e:
        print("\nError:", e)
