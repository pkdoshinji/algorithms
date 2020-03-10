#!/usr/bin/env python3

'''
Class that launches and maintains a random swarm of decoy servers.
These "will-o'-the-wisp" servers jump around continuously over a given
portnumber space at regular; they serve no purpose other than to confuse
and mislead network scanners (such as nmap).
'''

import socket
import random
import time
import threading


class Swarm:
    def __init__(self, occupied_ports, number, range_low=1, range_high=400, lifetime=10):
        self.occupied_ports = occupied_ports
        self.number = number
        self.range_low = range_low
        self.range_high = range_high
        self.lifetime = lifetime

    #Start up a server at a random port, avoiding numbers in the 'occupied_ports' attribute
    def server(self):
        while True:
            port = random.randrange(self.range_low, self.range_high) #portnumber space to be used; can range from 1 - 65535
            if port in self.occupied_ports:
                continue
            self.occupied_ports.append(port)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('', port))
            server.listen(5)
            server.close()
            self.occupied_ports.remove(port)

    def launch(self):
        ports_dict = {}  #Create a dictionary of thread names, one for each port
        for i in range(self.number):
            ports_dict[i] = f't{i}'

        for index in ports_dict: #Create and run a thread for each entry in jumping_ports_dict
            ports_dict[index] = threading.Thread(target=self.server)
            ports_dict[index].start()


s = Swarm([21,25,80], 50, 1, 65536)
s.launch()
