# -*- coding: utf-8 -*-
# Problem 35
# Circular primes

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.

# How many circular primes are there below one million?

from time import time
from UsefulFunctions import primes, is_prime, rotations

start_time = time()

p = primes()

candidate = next(p)
l = []
while candidate < 1000000:
    still_prime = True
    for e in rotations(candidate):
        if not is_prime(e):
            still_prime = False
            break

    if still_prime:
        l.append(candidate)

    candidate = next(p)

print l
print len(l)
l = filter(lambda x: str(x).count("0") == 0, l)  # 101, 103 etc. don't count
print l
print len(l)

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 21:12
# Solve by: 42604
# ---------------
# [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]
# 55
# Total Time:  5.95000004768
# [Finished in 6.1s]
