# -*- coding: utf-8 -*-
# Problem 72
# Counting fractions

# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 21 elements in this set.

# How many elements would be contained in the set of reduced proper fractions
# for d ≤ 1,000,000?

# 1. Sum the Euler totient function from φ(2) to φ(1000000)

from time import time

start_time = time()

limit = 1000000
phi = range(limit + 1)
for p in xrange(2, limit + 1):
    if phi[p] == p:             # a new prime
        for i in xrange(p, limit + 1, p):
            phi[i] = phi[i] / p * (p - 1)

count = sum(phi) - 1            # we have one extra at phi[1]
print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Sun, 30 Mar 2014, 05:17
# Solve by:  11305
# ---------------
# Answer: 303963552391
# Total Time:  1.63100004196
# [Finished in 1.9s]
