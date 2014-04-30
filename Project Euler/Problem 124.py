# -*- coding: utf-8 -*-
# Problem 124
# Ordered radicals

# The radical of n, rad(n), is the product of the distinct prime factors of n.
# For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.

# If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting
# on n if the radical values are equal, we get:

# http://projecteuler.net/problem=124

# Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and
# E(6) = 9.

# If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

from time import time

start_time = time()

# calculate rad(n)
N = 100000
numbers = [1 for i in xrange(N + 1)]
p = 2
rad = [(1, 0), (1, 1)]
while p <= N:
    if numbers[p] == 1:      # a new prime number
        for i in xrange(p, N + 1, p):
            numbers[i] *= p  # calculate rad(n)
    rad.append((numbers[p], p))
    p += 1

print "Answer:", sorted(rad)[10000][1]

print "Total Time: ", time() - start_time

# Completed on Tue, 29 Apr 2014, 23:48
# Solve by: 7906
# ---------------
# Answer: 21417
# Total Time:  0.233000040054
# [Finished in 0.4s]
