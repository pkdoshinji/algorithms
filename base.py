'''
Converts a (base M) number to a (base N) number where
extensions to bases eleven and greater are represented with
the capital letters of the Roman alphabet in the obvious
way, i.e., A=10, B=11, C=12, etc. (Compare the usual notation
for the hexadecimal numbers.) Restriction to the Arabic numerals
and the capital Roman alphabet imposes the restriction M, N <= 36.
'''

import sys

characters = '0123456789abcdefghijklmnopqrstuzwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/+'

#Usage: ./script <base M> <base N> <base M number>
M = int(sys.argv[1])
N = int(sys.argv[2])
M_number = sys.argv[3]

#Convert the (base M) number M_number to decimal
decimal = 0
for index in range(len(M_number)):
    value = characters.find(M_number[index])
    decimal += (value * (M**(len(M_number) - index - 1)))

#Get the Most Significant Digit of the number in (base N)
MSD = 0
while True:
    if (decimal // (N ** (MSD+1))) < 1:
        break
    MSD += 1

#Convert to (base N)
result = ''
for i in range((MSD),-1,-1):
    digit = decimal // (N**i)
    decimal = decimal % (N**i)
    result += characters[digit]

#Output
print(f'{M_number} (base {M}) converts to {result} (base {N})')