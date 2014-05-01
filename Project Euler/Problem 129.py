# -*- coding: utf-8 -*-
# Problem 129
# Repunit divisibility

# A number consisting entirely of ones is called a repunit. We shall define R(k)
# to be a repunit of length k; for example, R(6) = 111111.

# Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that
# there always exists a value, k, for which R(k) is divisible by n, and let A(n)
# be the least such value of k; for example, A(7) = 6 and A(41) = 5.

# The least value of n for which A(n) first exceeds ten is 17.

# Find the least value of n for which A(n) first exceeds one-million.

from time import time


def A(n):
    if n % 5 == 0:
        return 0

    R = 1
    k = 1
    while R != 0:
        R = (R * 10 + 1) % n
        k += 1

    return k

start_time = time()

limit = 1000000
n = 1000001
while A(n) < limit:
    n += 2

print "Answer:", n

print "Total Time: ", time() - start_time

# Completed on Thu, 1 May 2014, 03:38
# Solve by: 3354
# ---------------
# Answer: 1000023
# Total Time:  0.31500005722
# [Finished in 0.5s]
