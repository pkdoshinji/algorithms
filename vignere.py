#!/usr/bin/env python3

import sys
import argparse


class Vignere:

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    def __init__(self, key):
        self.key = key.upper()

    def process(self, message, mode='e'):
        # Encryption and decryption
        output = ''
        for i,j in zip(range(len(message)), range(len(message))):
            mssg_index = self.characters.find(message[i].upper())
            key_index = self.characters.find(self.key[j % len(self.key)].upper())
            if mode == 'e':
                code_index = (mssg_index + key_index) % len(self.characters)
            else:
                code_index = (mssg_index - key_index) % len(self.characters)
            output += self.characters[code_index]
        return output


def main():
    # Command line options (-c,-d,-i,-p,-o,-s,-g) with argparse module:
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encrypt", action="store_true", help="encrypt message")
    group.add_argument("-d", "--decrypt", action="store_true", help="decrypt message")
    parser.add_argument("-k", "--key", type=str, help="key string required as argument")
    parser.add_argument("-m", "--message", type=str, help="message string required as argument")

    args = parser.parse_args()

    # Set variables with command-line inputs
    encrypt = args.encrypt
    deploy = args.decrypt
    key = args.key
    message = args.message

    if encrypt:
        mode = 'e'
    else:
        mode = 'd'

    # Create Vignere object
    v = Vignere(key)
    print(f'Key: {v.key}')

    # Output
    text = v.process(message, mode)
    if mode == 'e':
        print(f'Ciphertext: {text}')
    else:
        print(f'Plaintext: {text}')


if __name__ == '__main__':
    main()
