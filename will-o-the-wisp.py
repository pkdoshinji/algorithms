#!/usr/bin/env python3

'''
Module that launches and maintains an arbitrary number of "will-o'-the-wisp"
servers. These decoy servers jump around at random over a given portnumber space at
regular intervals; they serve no purpose other than to confuse and mislead
network scanners (such as nmap).
'''

import socket
import random
import time
import threading


ports = [21, 22, 523] #These ports are already in use, we want to avoid them
jumping_ports = 10 #Number of jumping ports to create


#Start up a server at a random port, avoiding port numbers in the 'ports' list
def makeServer():
    global ports
    while True:
        port = random.randrange(1,400) #portnumber space to be used; can range from 1 - 65535
        if port in ports:
            continue
        ports.append(port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('', port))
        server.listen(5)
        time.sleep(10) #time (in seconds) before the next jump
        server.close()
        ports.remove(port)

def main():
    jumping_ports_dict = {}  #Create a dictionary of thread names, one for each port
    for i in range(jumping_ports):
        jumping_ports_dict[i] = f't{i}'

    for index in jumping_ports_dict: #Create and run a thread for each entry in jumping_ports_dict
        jumping_ports_dict[index] = threading.Thread(target=makeServer)
        jumping_ports_dict[index].start()

if __name__ == '__main__':
    main()