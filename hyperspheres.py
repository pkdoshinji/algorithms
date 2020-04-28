#!/usr/bin/env python3

from math import gamma, pi
import matplotlib.pyplot as plt
import numpy as np


class Hypersphere():
    def __init__(self, dimension, radius):
        self.dimension = dimension
        self.radius = radius

    def hypervolume(self):
        C = (pi**(self.dimension/2))/(gamma((self.dimension+2)/2))
        return C*(self.radius**self.dimension)

    def hypersurface(self):
        C = (self.dimension*(pi**(self.dimension/2)))/(gamma((self.dimension+2)/2))
        return C*(self.radius**(self.dimension-1))


radii = [i for i in range(1,40)]
volumes = []
areas = []

for j in range(1,40):
    # Run through dimension values and calculate area & volume
    S = Hypersphere(j,1)
    volumes.append(S.hypervolume())
    areas.append(S.hypersurface())

# Plot area & volume vs. dimension
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(radii,volumes, color='b', label='Hypervolume')
ax.plot(radii,areas, color='r', label='Hypersurface area')
ax.legend()
plt.title('Properties of Hyperspheres (r=1)', fontweight='bold')
plt.xlabel('Dimension of Hypersphere')
plt.ylabel('Area/Volume')
plt.show()
