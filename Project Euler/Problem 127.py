# -*- coding: utf-8 -*-
# Problem 127
# abc-hits

# The radical of n, rad(n), is the product of distinct prime factors of n. For
# example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.

# We shall define the triplet of positive integers (a, b, c) to be an abc-hit
# if:

#     GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
#     a < b
#     a + b = c
#     rad(abc) < c

# For example, (5, 27, 32) is an abc-hit, because:

#     GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
#     5 < 27
#     5 + 27 = 32
#     rad(4320) = 30 < 32

# It turns out that abc-hits are quite rare and there are only thirty-one
# abc-hits for c < 1000, with ∑c = 12523.

# Find ∑c for c < 120000.

# 1. GCD(a,b) = 1 -> GCD(a,c) = 1 & GCD(b,c) = 1
# 2. rad(abc) = rad(a) * rad(b) * rad(c)

from time import time
import fractions as F

start_time = time()

# calculate rad(n)
N = 120000
numbers = [1 for i in xrange(N + 1)]
p = 2
rad = [1, 1]    # rad(0) & rad(1)
while p <= N:
    if numbers[p] == 1:      # a new prime number
        for i in xrange(p, N + 1, p):
            numbers[i] *= p  # calculate rad(n)
    rad.append(numbers[p])
    p += 1

sum_ = 0
for a in xrange(1, N):
    for b in xrange(a + 1, N - a + 1):
        if rad[a] * rad[b] * rad[a + b] >= a + b:
            continue
        if F.gcd(a, b) == 1:
            sum_ += a + b

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Thu, 1 May 2014, 01:07
# Solve by: 3124
# ---------------
# Answer: 18407904
# Total Time:  2509.91200018
# [Finished in 2510.1s]
