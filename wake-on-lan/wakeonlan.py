#!/usr/bin/env python3

# https://apple.stackexchange.com/questions/95246/wake-other-computers-from-mac-osx

# import socket
# import sys

# if len(sys.argv) < 3:
#    print "Usage: wakeonlan.py <ADR> <MAC>     (example: 192.168.1.255 00:11:22:33:44:55)"
#    sys.exit(1)

# mac = sys.argv[2]
# data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.sendto(data.decode("hex"), (sys.argv[1], 9))

# updated version
import socket
import sys
import codecs

if len(sys.argv) < 3:
    print("Usage: wakeonlan.py <ADR> <MAC>     (example: 192.168.1.255 00:11:22:33:44:55)")
    sys.exit(1)

mac = sys.argv[2]
data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
decode_hex = codecs.getdecoder("hex_codec")
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(decode_hex(data)[0], (sys.argv[1], 9))


