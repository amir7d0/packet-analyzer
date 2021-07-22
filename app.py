import socket
import struct
import textwrap
import time
import binascii

class Ethernet:
    def __init__(self, r_data):
        dest, src, proto = struct.unpack('!6s6sH', r_data[:14])

        self.dest_mac = get_mac_addr(dest)
        self.src_mac = get_mac_addr(src)
        self.proto = proto
        self.data = r_data[14:]
