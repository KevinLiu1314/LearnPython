# -*- coding: utf-8 -*-
# Almost equilateral triangles
# Problem 94

# It is easily proved that no equilateral triangle exists with integral length
# sides and integral area. However, the almost equilateral triangle 5-5-6 has an
# area of 12 square units.

# We shall define an almost equilateral triangle to be a triangle for which two
# sides are equal and the third differs by no more than one unit.

# Find the sum of the perimeters of all almost equilateral triangles with
# integral side lengths and area and whose perimeters do not exceed one billion
# (1,000,000,000).

from time import time
import math


def almost_equilateral(leg):
    """
    if triangle (leg, leg, leg+1) or (leg, leg, leg-1) has integral area,
    return the perimeter, else return 0
    """
    leg_squared = leg ** 2

    # case 1, third side is 1 more than the "leg"
    base = leg + 1
    height = math.sqrt(leg_squared - (base / 2.) ** 2)
    if (base * int(height) / 2) == int(base * height / 2):
        return leg * 3 + 1

    # case 2, third side is 1 less than the "leg"
    base = leg - 1
    height = math.sqrt(leg_squared - (base / 2.) ** 2)
    if (base * int(height) / 2) == int(base * height / 2):
        return leg * 3 - 1

    return 0

start_time = time()

perimeter_sum = 0
for leg in xrange(2, (1000000000 - 1) / 3 + 1):
    perimeter_sum += almost_equilateral(leg)

print "Answer:", perimeter_sum

print "Total Time: ", time() - start_time

# Completed on Mon, 31 Mar 2014, 03:42
# Solve by: 
# ---------------
