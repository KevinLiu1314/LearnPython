# -*- coding: utf-8 -*-
# Problem 123
# Prime square remainders

# Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when
# (pn−1)^n + (pn+1)^n is divided by pn^2.

# For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

# The least value of n for which the remainder first exceeds 10^9 is 7037.

# Find the least value of n for which the remainder first exceeds 10^10.

# from time import time

# 1. make use of Problem 120
# 2. r = 2*pn


def primes():
    n = 2
    yield n

    n = 3
    yield n

    primes_so_far = [2, 3]      # takes care of index out of range case
                                # when n = 3 if initial is only [2]
    while True:
        n += 1
        divisor_index = 0
        is_prime = False
        while n % primes_so_far[divisor_index] != 0:
            divisor_index += 1
            if primes_so_far[divisor_index] ** 2 > n:
                is_prime = True
                break

        if is_prime:
            yield n
            primes_so_far.append(n)

from time import time

start_time = time()

n = 0
pgen = primes()     # prime generator
while True:
    n += 1
    p = next(pgen)
    if n % 2 == 0:  # if n is even, the remainder is always 2
        r = 2
    else:
        r = (2 * p * n)
    if r > 10000000000:
        break

print "Answer:", n

print "Total Time: ", time() - start_time

# Completed on Sat, 5 Apr 2014, 04:39
# Solve by: 6375
# ---------------
# Answer: 21035
# Total Time:  0.72000002861
# [Finished in 0.9s]
