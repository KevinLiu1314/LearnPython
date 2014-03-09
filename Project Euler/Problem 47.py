# -*- coding: utf-8 -*-
# Problem 47
# Distinct primes factors

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?

from time import time
from UsefulFunctions import primes


def has_four_dpf(n):
    """
    Return True if n has 4 distinct prime factors,
    make uses of a prebuild prime list name "plist" that has primes under 1000000
    """
    i = 0       # index into the plist
    distinct_count = 0
    while True:
        while n != 1:
            if n % plist[i] == 0:
                while n % plist[i] == 0:    # factor out current prime number
                    n /= plist[i]
                distinct_count += 1
                if distinct_count > 4:
                    return False

            i += 1

        return distinct_count == 4

start_time = time()

pgen = primes()     # prime generator
p = next(pgen)
plist = []
while p < 1000000:
    plist.append(p)
    p = next(pgen)

# start with i=10 and check at each iteration if i, i+1, i+2, i+3 all have
# 4 distinct prime factors, when found, print i and exit loop
# h4dpf1 = has 4 distinct prime factor 1
# don't start at has_four_dpf(0), the function will get into a infinite loop
h4dpf1 = has_four_dpf(1)
h4dpf2 = has_four_dpf(2)
h4dpf3 = has_four_dpf(3)
h4dpf4 = has_four_dpf(4)
i = 4
while True:
    if h4dpf1 == h4dpf2 == h4dpf3 == h4dpf4 == True:
        print h4dpf1, h4dpf2, h4dpf3, h4dpf4
        print i - 3     # this is the 4th one, we need the first number
        break

    i += 1

    h4dpf1, h4dpf2, h4dpf3, h4dpf4 = h4dpf2, h4dpf3, h4dpf4, has_four_dpf(i)

print "Total Time: ", time() - start_time

# Completed on Sat, 8 Mar 2014, 21:39
# Solve by:  27813
# ---------------
# True True True True
# 134043
# Total Time:  23.9510002136
# [Finished in 24.1s]
