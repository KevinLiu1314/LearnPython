# -*- coding: utf-8 -*-
# Problem 100
# Arranged probability

# If a box contains twenty-one coloured discs, composed of fifteen blue discs
# and six red discs, and two discs were taken at random, it can be seen that the
# probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

# The next such arrangement, for which there is exactly 50% chance of taking two
# blue discs at random, is a box containing eighty-five blue discs and
# thirty-five red discs.

# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000
# discs in total, determine the number of blue discs that the box would contain.

# solve b/n * (b-1)/(n-1) = 1/2 for b in terms of n
# use the quadratic formula

from time import time
import math


def psquare():
    """
    Perfect square: return a number > 1000000000000 that's a perfect square
    """
    i = 2828427124744
    while True:
        i += 1
        yield i ** 2

start_time = time()

psquaregen = psquare()

det = 1.1     # make sure the while loop gets run for the first p
while int(math.sqrt(det)) ** 2 != det:
    p = next(psquaregen)
    det = 64 - 32 * (4 - p)

n = (8 + math.sqrt(det)) / 16

b = (2 + math.sqrt(4 + 8 * n * (n - 1))) / 4

print "n: %f  b: %f" % (n, b)

print "Total Time: ", time() - start_time

# Completed on Fri, 14 Mar 2014, 03:44
# Solve by: 12701
# ---------------
#