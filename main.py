import pyfiglet

import os
import sys
import socket
from socket import gethostbyname, getservbyname, getservbyport

project_banner = pyfiglet.figlet_format("TCP PORT SCANNER")
print(project_banner)

try:
    hostname = sys.argv[1]
    port_lowerbound = int(sys.argv[2])
    port_upperbound = int(sys.argv[3])
    
    target = socket.gethostbyname(sys.argv[1])
except IndexError:
    print("Error: Invalid number of arguments. Expected 3")

print(f'\nScanning target: {target} ({hostname})\n')

print("Port open\tService")
print('-' * 25)

for port in range(port_lowerbound, port_upperbound):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1) # what is this ?

    res = s.connect_ex((target, port))

    if res == 0:
        # print(f'{port}')
        try:
            service = getservbyport(port, 'tcp')
            print(f'{port}\t\t{service}')
        except OSError:
            print(f'{port}')
    else:
        pass
    s.close()

