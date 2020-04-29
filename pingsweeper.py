#!/usr/bin/env python3

import sys
from scapy.all import *

conf.verb = 0

ips = []

def ping(dest_ip):
    p = sr1(IP(dst=dest_ip,ttl=10)/ICMP(), timeout=2)
    if p != None:
        return dest_ip
    else:
        return None

def main():
    raw = sys.argv[1].split('.')
    subnet_raw = f'{raw[0]}.{raw[1]}.{raw[2]}'

    print('[*] Scanning in progress...')
    for i in range(1,256):
        subnet = f'{subnet_raw}.{i}'
        response = ping(subnet)
        if response != None:
            ips.append(response)


    print('\nThe following IPs are up:')
    for item in ips:
        print(f'    {item}')

    print('\n[*] Finished scanning!')

if __name__ == '__main__':
    main()
