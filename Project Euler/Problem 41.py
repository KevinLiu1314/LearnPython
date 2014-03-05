# -*- coding: utf-8 -*-
# Problem 41
# Pandigital prime

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.

# What is the largest n-digit pandigital prime that exists?


from time import time
from UsefulFunctions import primes, is_prime
from itertools import permutations


def pandigitals():
    for n in sorted(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]), reverse=True):
        yield n
    for n in sorted(permutations([1, 2, 3, 4, 5, 6, 7, 8]), reverse=True):
        yield n
    for n in sorted(permutations([1, 2, 3, 4, 5, 6, 7]), reverse=True):
        yield n
    for n in sorted(permutations([1, 2, 3, 4, 5, 6]), reverse=True):
        yield n
    for n in sorted(permutations([1, 2, 3, 4, 5]), reverse=True):
        yield n
    for n in sorted(permutations([1, 2, 3, 4]), reverse=True):
        yield n

start_time = time()

# Method 1 - takes too long, it's so stupid, needs to wait till beyond 987654321
# p = primes()
# c = next(p)
# answer = 0
# while c < 987654321:
#     if pandigital(c):
#         answer = c
#     c = next(p)

p = pandigitals()
while True:
    raw_n = next(p)
    if raw_n[-1] % 2 == 0 or raw_n[-1] == 5:    # filter out the even & 5 ending
        continue                                # takes .5 seconds off
    n = reduce(lambda x, y: 10 * x + y, raw_n)
    if is_prime(n):
        print n
        break

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 23:58
# Solve by: 33179
# ---------------
# 7652413
# Total Time:  0.734999895096
# [Finished in 0.9s]
