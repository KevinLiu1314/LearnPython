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
sum_ = 0
p = 2
while p <= n:
    if numbers[p] == 0:      # a new prime number
        for i in range(p, n + 1, p):
            if i <= n - k or i > k:
                numbers[i] += pf_sum(i, p)  # add prime factor sum to number
            else:
                numbers[i] = 1  # skipping only works because we have two ranges
                                # that are not overlaping
                                # 1 to 5M, 15M+1 to 20M
                                # this saves about 20 seconds
    if p <= n - k:
        sum_ += -numbers[p]
    elif p > k:
        sum_ += numbers[p]

    p += 1

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Sat, 10 May 2014, 02:52
# Solve by: 3288
# ---------------
# Answer: 7526965179680
# Total Time:  52.7799999714
# [Finished in 53.6s]
