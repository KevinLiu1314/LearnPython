# -*- coding: utf-8 -*-
# Problem 77
# Prime summations

# It is possible to write ten as the sum of primes in exactly five different
# ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of primes in over five
# thousand different ways?

from time import time


def sieve(N):
    """
    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the first prime number.
    3. Starting from p, enumerate its multiples by counting to n in increments
       of p, and mark them in the list (these will be 2p, 3p, 4p, etc.; the p
       itself should not be marked).
    4. Find the first number greater than p in the list that is not marked.
       If there was no such number, stop. Otherwise, let p now equal this new
       number (which is the next prime), and repeat from step 3.
    """
    numbers = [1 for i in xrange(N + 1)]
    p = 2
    while p <= N:
        if numbers[p] == 1:     # a new prime number
            yield p
            for j in range(p, N + 1, p):
                numbers[j] = 0  # a multiple of p, not a prime
            numbers[p] = 1      # save our prime
        p += 1

start_time = time()

primes = [p for p in sieve(1000)]   # should be enough primes
n = 2
while True:
    ways = [0] * (n + 1)
    ways[0] = 1

    for i in xrange(len(primes)):
        if primes[i] > n:
            break
        for j in xrange(primes[i], n + 1):
            ways[j] += ways[j - primes[i]]

    if ways[n] > 5000:
        break

    if n == 10:
        print ways

    n += 1


print "Answer:", n

print "Total Time: ", time() - start_time

# Completed on Thu, 17 Apr 2014, 23:14
# Solve by: 9426
# ---------------
# Answer: 71
# Total Time:  0.0090000629425
# [Finished in 0.2s]
