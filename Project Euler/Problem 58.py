# -*- coding: utf-8 -*-
# Problem 58
# Spiral primes

# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued, what is the
# side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

from time import time
from UsefulFunctions import is_prime
import math


def diagonal_numbers():
    """
    Generate a stream of diagonal numbers, and indicate if a layer of the grid
    has been completed.
    """
    steps = 1
    n = 1
    yield n, True           # the first layer, 1 by itself
    while True:
        n += 1 + steps       # diagonal number at upper right corner
        yield n, False

        steps += 1
        n += steps
        yield n, False      # diagonal number at upper left corner

        n += steps
        yield n, False      # diagonal number at lower left corner

        n += steps          # diagonal number at lower right corner
        yield n, True       # this completes one layer of the grid

        steps += 1          # step size for next layer


start_time = time()

dgen = diagonal_numbers()   # diagonal number generator
diagonal_numbers = 0
diagonal_primes = 0

while True:
    n, completed = next(dgen)
    diagonal_numbers += 1
    if is_prime(n):
        diagonal_primes += 1
    if completed and n > 7:     # grid length must be larger than 7
        if float(diagonal_primes)/diagonal_numbers < 0.10:
        #if diagonal_primes < int(diagonal_numbers * 0.10):   # this gives incorrect answer
            print "len: %d  primes: %d,  numbers: %d  percent: %f" % (math.sqrt(n), diagonal_primes, diagonal_numbers, float(diagonal_primes)/diagonal_numbers)
            break

print "the number is", n

print "Total Time: ", time() - start_time

# Completed on Tue, 11 Mar 2014, 23:38
# Solve by: 19721
# ---------------
# len: 26241  primes: 5248,  numbers: 52481  percent: 0.099998
# the number is 688590081
# Total Time:  21.6649999619
# [Finished in 21.8s]

# The following is obtained by using "if diagonal_primes < int(diagonal_numbers * 0.10):"
# The answer is off by 3 layers
# len: 26247  primes: 5248,  numbers: 52493  percent: 0.099975
# the number is 688905009
# Total Time:  21.5050001144
# [Finished in 21.7s]
