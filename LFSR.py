'''
Python class for the instantiation of a Linear Feedback Shift Register data
type. The seed attribute is the initialization value for the LFSR. It also
determines the length (number of bits) of the LFSR and is entered as a
string of 1s and 0s. The coefficients input is likewise a string of 1s and
0s. These values correspond to the coefficients c0, c1, ... cn in the
standard mathematical description of LFSRs.
'''

class LFSR:

    def __init__(self, seed, coefficients):
        self.length = len(seed)
        self.coefficients = [int(item) for item in coefficients]
        self.state = [int(item) for item in seed]

    def increment(self):
        newbit = 0
        for index in range(len(self.coefficients)):
            newbit = newbit ^ (self.coefficients[index] & self.state[index])
        self.state.append(newbit)
        out = self.state.pop(0)
        return out

