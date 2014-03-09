# -*- coding: utf-8 -*-
# Problem 46
# Goldbach's other conjecture

# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

from time import time
from UsefulFunctions import primes, is_prime


def ocgen():
    n = 9
    while True:
        if not is_prime(n):
            yield n
        n += 2

start_time = time()

oc = ocgen()            # odd composite stream
continue_ = True
while continue_:
    c = next(oc)        # get an odd composite candidate
    pgen = primes()     # start with 1st prime all over again

    while True:         # verification loop
        p = next(pgen)  # try a new prime number
        i = 1
        while p + 2 * (i ** 2) < c: # try to see if an i could make the current prime work
            i += 1

        if p + 2 * (i ** 2) == c:   # if formula is verified, break 
            break

        if p > c:       # the formula fails
            continue_ = False
            break

print c

print "Total Time: ", time() - start_time

# Completed on Wed, 5 Mar 2014, 20:02
# Solve by:  28838
# ---------------
# 5777
# Total Time:  2.15499997139
# [Finished in 2.4s]
