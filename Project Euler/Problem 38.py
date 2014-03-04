# -*- coding: utf-8 -*-
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

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

# [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# 748317
# Total Time:  2.70900011063
# [Finished in 2.9s]
