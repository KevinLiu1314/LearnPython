# -*- coding: utf-8 -*-
# Problem 231
# The prime factorisation of binomial coefficients

# The binomial coefficient 10C3 = 120.
# 120 = 23 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.
# So the sum of the terms in the prime factorisation of 10C3 is 14.

# Find the sum of the terms in the prime factorisation of 20000000C15000000.

# nCr = n!/k!/(n-k)!
# 20000000C15000000 = 20000000!/15000000!/5000000!
# Add the prime factors of the numbers between 15M+1 and 20M, and substract
# the sum of the prime factors of the numbers between 1 and 5M.


def pf_sum(n, p):
    nof = 0     # number of factors
    while n % p == 0:
        nof += 1
        n /= p
    return nof * p

from time import time

start_time = time()

n = 20000000
k = 15000000
numbers = [0 for i in xrange(n + 1)]
p = 2
while p <= n:
    if numbers[p] == 0:      # a new prime number
        for i in range(p, n + 1, p):
            numbers[i] += pf_sum(i, p)  # add prime factor sum to number
    p += 1

fsnmk = 0   # factor sum of (n minus k)!
for i in xrange(1, n-k+1):
    fsnmk += numbers[i]

fsnfdkf = 0     # factor sum of n! divided by k!
for i in xrange(k+1, n+1):
    fsnfdkf += numbers[i]

print "Answer:", fsnfdkf - fsnmk

print "Total Time: ", time() - start_time

# Completed on Sat, 10 May 2014, 02:52
# Solve by: 3288
# ---------------
# Answer: 7526965179680
# Total Time:  68.5600001812
# [Finished in 70.4s]
