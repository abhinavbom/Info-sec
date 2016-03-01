__author__ = 'darklord'

import socket
import thread
import sys


def port_scanner(ip):
    print "-" * 60
    print "Please wait, scanning remote host", ip
    print "-" * 60
    port = 0
    try:
        for port in range(1,1000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((ip, port))
            if result == 0:
                print "Port %d is open",port
            s.close()
    except KeyboardInterrupt:
        sys.exit()

#get server details

if __name__ == "__main__":
    host = raw_input("enter the remote server to scan:")
    #hostIP = socket.getservbyname(host)
    port_scanner(host)
