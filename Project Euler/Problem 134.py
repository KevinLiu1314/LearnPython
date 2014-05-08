# -*- coding: utf-8 -*-
# Problem 134
# Prime pair connection

# Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
# 1219 is the smallest number such that the last digits are formed by p1 whilst
# also being divisible by p2.

# In fact, with the exception of p1 = 3 and p2 = 5, for every pair of
# consecutive primes, p2 > p1, there exist values of n for which the last digits
# are formed by p1 and n is divisible by p2. Let S be the smallest of these
# values of n.

# Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

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

primes = [p for p in sieve(1000000)]   # primes between 5 & 1000000
del primes[0:2]

sum_ = 0
for i in xrange(len(primes) - 1):
    p1 = primes[i]
    p2 = primes[i + 1]
    n = 1
    while int(str(n) + str(p1)) % p2 != 0:
        n += 1
    sum_ += n

sum_ = 0

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Wed, 30 Apr 2014, 04:06
# Solve by: 
# ---------------
# takes too long!