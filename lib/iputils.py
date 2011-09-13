from socket import inet_aton, inet_ntoa
from struct import pack, unpack

def ip2long(ip_addr):
    ip_packed = inet_aton(ip_addr)
    ip = unpack("!L", ip_packed)[0]
    return ip

def long2ip(long):
    packed_long = pack('!L', long)
    ip = inet_ntoa(packed_long)
    return ip
