# -*- coding: utf-8 -*-
# Problem 37
# Truncatable primes

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime at
# each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from time import time
from UsefulFunctions import primes, is_prime


def truncatable(n):
    # test for left truncatable
    n_str = str(n)

    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False

    # test for right truncatable
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[:i])):
            return False

    return True

start_time = time()

pstream = primes()

for i in range(4):      # skip first 4 primes
    p = next(pstream)

l = []
while True:
    p = next(pstream)
    if truncatable(p):
        l.append(p)
        if len(l) == 11:    # found all, we are done
            break

print l
print sum(l)

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 21:54
# Solve by: 35992
# ---------------
# [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# 748317
# Total Time:  2.70900011063
# [Finished in 2.9s]
