# -*- coding: utf-8 -*-
# Problem 108
# Diophantine reciprocals I

# In the following equation x, y, and n are positive integers.
# 1/x + 1/y = 1/n

# For n = 4 there are exactly three distinct solutions:

# 1/5 + 1/20 = 1/4
# 1/6 + 1/12 = 1/4
# 1/8 + 1/8 = 1/4

# What is the least value of n for which the number of distinct solutions
# exceeds one-thousand?

# NOTE: This problem is an easier version of problem 110; it is strongly advised
# that you solve this one first.

# http://www.mathblog.dk/project-euler-125-square-sums-palindromic/

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


def factors_of_n_squared(n):
    i = 0
    number_of_factors = 1
    r = n
    while r != 1:
        exponents = 0
        if primes[i] ** 2 > n:
            break
        while r % primes[i] == 0:
            exponents += 1
            r /= primes[i]
        number_of_factors *= 2 * exponents + 1

        i += 1

    return number_of_factors

start_time = time()

primes = [p for p in sieve(1000)]   # should be enough primes

n = 1
N = 1000
while (factors_of_n_squared(n) + 1) / 2 <= N:
    n += 1

print "Answer:", n

print "Total Time: ", time() - start_time

# Completed on Wed, 30 Apr 2014, 04:06
# Solve by: 7140
# ---------------
# Answer: 180180
# Total Time:  4.22800016403
# [Finished in 4.4s]
