#!/usr/bin/env python3

'''Plot the cosine series of -(1+cos(theta_n*log(x))), where theta_n are the
zeros on the critical line Re(s) = 0.5 of the Riemann zeta function. The resulting
function has peaks at prime powers of x.
'''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def get_list(filename):
    fh = open(filename)
    my_list = fh.readlines()
    return [float(item.strip()) for item in my_list]


spectrum_list = get_list('spectrum.txt') # Zeros of the Riemann Zeta
use_list = spectrum_list[:1000] # Use only a selection

xvals = np.linspace(2,100,10000)
yvals = -1

#yvals += -(np.log(i) / (i ** (0.5)) * (np.cos(xvals * np.log(i))))
for theta in use_list:
    yvals -= np.cos(np.log(xvals)*theta)

plt.plot(xvals, yvals)
plt.show()
