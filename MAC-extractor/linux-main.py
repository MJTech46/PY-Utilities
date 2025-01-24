import socket
import fcntl
import struct

def get_mac_address_using_socket(interface="eth0"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(sock.fileno(), 0x8927, struct.pack('256s', interface[:15].encode('utf-8')))
    return ':'.join(f"{b:02x}" for b in info[18:24])

# Example usage
print("MAC Address using socket:", get_mac_address_using_socket("eth0"))
