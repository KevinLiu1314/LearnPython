# -*- coding: utf-8 -*-
# Problem 32
# Pandigital products

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

from time import time
from itertools import permutations


def raw(digits):
    for size in range(1, len(digits) + 1):
        for number in permutations(digits, size):
            yield number


start_time = time()

l = []

for multiplicand in raw([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    for multiplier in raw(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(multiplicand)):
        x = int(''.join(str(d) for d in multiplicand))
        y = int(''.join(str(d) for d in multiplier))
        product = x * y
        identity = str(x) + str(y) + str(product)
        if identity.count('0') > 0:
            continue
        if len(identity) < 9:
            continue
        elif len(identity) > 9:
            break
        else:
            if not product in l and len(set(identity)) == 9:
                l.append(product)

print sum(l)

print "Total Time: ", time() - start_time

# 45228
# Total Time:  10.254999876
# [Finished in 10.4s]
