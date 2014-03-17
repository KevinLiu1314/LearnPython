# -*- coding: utf-8 -*-
# Problem 145
# How many reversible numbers are there below one-billion?

# Some positive integers n have the property that the sum [ n + reverse(n) ]
# consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
# 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and
# 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (10^9)?

from time import time


def is_reversible(n):
    if n % 10 == 0:
        return False

    reverse_n = 0
    t = n       # use to calculate the reverse number
    while t > 0:
        d = t % 10
        reverse_n = reverse_n * 10 + d
        t /= 10

    sum_ = n + reverse_n
    while sum_ > 0:
        d = sum_ % 10
        if d % 2 == 0:
            return False
        sum_ /= 10

    return True

start_time = time()

count = 0
for i in xrange(1, 1000000000, 2):    # only checking odd numbers, its partner
    if is_reversible(i):        # will alway be even, so we'll double the count
        count += 1

print "Total: ", count * 2

print "Total Time: ", time() - start_time

# Completed on Thu, 13 Mar 2014, 01:54
# Solve by: 8735
# ---------------
# Total:  608720
# Total Time:  1792.96099997
# [Finished in 1793.1s]
