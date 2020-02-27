#!/usr/bin/env python3
'''
A module for converting a (positive) decimal number to its (base N) equivalent, where
extensions to bases eleven and greater are represented with the capital letters
of the Roman alphabet in the obvious way, i.e., A=10, B=11, C=12, etc. (Compare
the usual notation for the hexadecimal numbers.) The decimal number and the
base (N) are entered in the command line: baser.py <base> <decimal number to convert>
'''

import sys


#Character set for representing digits. For (base N) the set is characters[:N]
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'


#Usage guidelines
def usage():
    print('[**]Usage: baser.py <base> <number to convert>')
    print(f'           <base> must be less than or equal to {len(characters)}')
    print(f'           <number> must be a nonnegative integer')


#Get the most significant digit (MSD) of the decimal number in (base N)
def getMSD(base, number):
    MSD = 1
    while True:
        if (base ** MSD) > number:
            return MSD
        MSD += 1


#Convert the decimal number to (base N)
def convert(MSD, base, number):
    result = ''
    for i in range(MSD - 1, -1, -1):
        value = number // (base ** i)
        result += chars[value]
        number = number % (base ** i)
    return result


def main():
    #Input sanitization
    try:
        base = int(sys.argv[1])
    except:
        usage()
        exit()
    try:
        number = int(sys.argv[2])
    except:
        usage()
        exit()
    if base > len(characters):
        usage()
        exit(0)
    if number == 0:
        print(0)
        exit(0)
    if number < 0:
        usage()
        exit(0)

    global chars
    chars = characters[:base] #Get the (base N) character set
    print(convert(getMSD(base, number), base, number)) #Convert and output

if __name__ == '__main__':
    main()
