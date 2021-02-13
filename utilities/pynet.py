#!/user/bin/new python3
#python netowork
#

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_add = socket.gethostbyname(host_name)
    print "Host name: %s " % host_name
    print "Ip address : %s " % ip_add

if __name__ = '__main__':
    print_machine_info()