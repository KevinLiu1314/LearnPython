# -*- coding: utf-8 -*-
# Problem 187
# Semiprimes

# A composite is a number containing at least two prime factors. For example,
# 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

# There are ten composites below thirty containing precisely two, not
# necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# How many composite integers, n < 10^8, have precisely two, not necessarily
# distinct, prime factors?

from time import time
from UsefulFunctions import primes
import array

start_time = time()

N = 100000000
factors = array.array("B", [0 for i in xrange(N + 1)])  # if not using xrange, memory will blow up!

pgen = primes()
p = next(pgen)
while p <= N / 2:
    for i in xrange(p, N, p):
        factors[i] += 1         # new factor
        if i % p ** 2 == 0:     # same factor twice?
            factors[i] += 1
            if i % p ** 3 == 0: # three or more same factors?
                factors[i] += 1
    p = next(pgen)

count = 0
for i in range(N):
    if factors[i] == 2:
        count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Thu, 27 Mar 2014, 02:24
# Solve by: 6293
# ---------------
# Answer: 17427258
# Total Time:  825.401000023
# [Finished in 826.5s]
