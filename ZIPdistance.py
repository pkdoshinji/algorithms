#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''ZIPdistance is a command-line tool that calculates the great circle
distance between any two ZIP codes using the haversine formula:

hav(THETA) = hav(phi_2 - phi_1) + cos(phi_1)cos(phi_2)hav(lambda_2 - lambda_1)

where hav(theta) = sin(theta/2)**2 and distance = 2*radius*arcsin(hav(THETA)**0.5).

The ZIP code arguments are to be entered as commandline arguments. For example:

./ZIPdistance.py 11225 86336

This yields:

The distance from 11225 (Brooklyn, NY) to 86336 (Sedona, AZ) is:
3361.91 kilometers / 2088.994 miles

Author: Patrick Kelly
Last revised: April 22, 2020
'''

import csv
import sys
import numpy as np

earth_mean_radius = 6.3710088e6
km_to_miles = 0.621371

ZIP_dict = {}

# Haversine function
def haversine(theta):
    return np.sin(theta/2)**2

# Calculate great circle distance
def great_circle_distance(latitude1, longitude1, latitude2, longitude2):

    #Convert degrees to radians
    lat1 = np.radians(latitude1)
    long1 = np.radians(longitude1)
    lat2 = np.radians(latitude2)
    long2 = np.radians(longitude2)

    delta_lat = lat2 - lat1
    delta_long = long2 - long1

    a = haversine(delta_lat) + (np.cos(lat1) * np.cos(lat2) * (haversine(delta_long)))
    c = 2 * (np.arctan2(np.sqrt(a), np.sqrt(1 - a)))

    return earth_mean_radius * c

# Populate a dictionary from csv file
def get_ZIP_dict():
    with open('ZIPcodes.csv') as fh:
        reader = csv.reader(fh)
        header = next(fh)

        for record in reader:
            record_list = record[0].split(';')
            ZIP_dict[record_list[0]] = (record_list[1], record_list[2], float(record_list[3]), float(record_list[4]))

    return ZIP_dict


def main():
    ZIP_dict = get_ZIP_dict()
    ZIP1 = ZIP_dict[sys.argv[1]]
    ZIP2 = ZIP_dict[sys.argv[2]]
    dist = great_circle_distance(ZIP1[2], ZIP1[3], ZIP2[2], ZIP2[3])
    print(f'The distance from {sys.argv[1]} ({ZIP1[0]}, {ZIP1[1]}) '
          f'to {sys.argv[2]} ({ZIP2[0]}, {ZIP2[1]}) is:')
    print(f'{round(dist*0.001,3)} kilometers / {round(km_to_miles*dist*0.001,3)} miles')


if __name__ == '__main__':
    main()




