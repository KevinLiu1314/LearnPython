# -*- coding: utf-8 -*-
# Problem 87
# Prime power triples

# The smallest number expressible as the sum of a prime square, prime cube, and
# prime fourth power is 28. In fact, there are exactly four numbers below fifty
# that can be expressed in such a way:

# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4

# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?


def is_expressible(n):
    i = 0
    while i < len(p_square) and p_square[i] < limit:
        j = 0
        while j < len(p_cube) and p_square[i] + p_cube[j] < limit:
            if n - p_square[i] - p_cube[j] in p_four:
                return True
            j += 1

        i += 1

    return False

from time import time
from UsefulFunctions import primes

start_time = time()

limit = 50000000
pgen = primes()     # prime generator
p = next(pgen)
p_square = []       # prime squares
p_cube = []         # prime cubes
p_four = []         # prime fourth power
while p ** 2 < limit:
    p_square.append(p ** 2)
    if p ** 3 < limit:
        p_cube.append(p ** 3)
        if p ** 4 < limit:
            p_four.append(p ** 4)
    p = next(pgen)

count = 0
for i in xrange(1, limit):
    if is_expressible(i):
        count += 1

print count

print "Total Time: ", time() - start_time

# Completed on Thu, 13 Mar 2014, 02:26
# Solve by: 15751
# ---------------

# This took more than 4 hours without any result
