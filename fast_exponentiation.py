import sys

def get_parameters():
    number = int(sys.argv[1])
    expo = int(sys.argv[2])
    modulus = int(sys.argv[3])
    return number, expo, modulus

def int_to_bit(integer):
    #Convert exponent to binary string
    binary = str(bin(integer))[2:]
    return binary

def modular_expo(number, exponent, modulus):
    #Fast exponentiation algorithm
    result = number #initialize result
    expo_bits = int_to_bit(exponent)
    for index in range(1, len(expo_bits)):
        result = (result**2)%modulus
        if expo_bits[index] == '1':
            result = (result*number)%modulus
    return result

def main():
    number, expo, modulus = get_parameters()
    print(modular_expo(number, expo, modulus))

if __name__ == '__main__':
    main()