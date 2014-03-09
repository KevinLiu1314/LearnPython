# -*- coding: utf-8 -*-
# Problem 53
# Combinatoric selections

# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,
# nCr = n!/(r!(n−r)!), where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100,
# are greater than one-million?

from time import time
import math


def nCr(n, r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

start_time = time()

count = 0
for n in range(23, 101):
    for r in range(1, n):
        if nCr(n, r) > 1000000:
            count += 1

print count

print "Total Time: ", time() - start_time

# Completed on Wed, 5 Mar 2014, 21:00
# Solve by:  30765
# ---------------
# 4075
# Total Time:  0.069000005722
# [Finished in 0.2s]
