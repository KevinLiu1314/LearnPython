# -*- coding: utf-8 -*-
# Problem 179
# Consecutive positive divisors

# Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same
# number of positive divisors. For example, 14 has the positive divisors
# 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

from time import time


def factors(n):
    """ return the number of factors in n"""
    f = 1

    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            f += 1
            if d != n / d:
                f += 1
        d += 1

    return f

start_time = time()

n = 2
count = 0
fn = factors(n)
fn1 = factors(n + 1)
while n < 10000000:
    if fn == fn1:
        count += 1

    n += 1
    fn = fn1
    fn1 = factors(n)

print count

print "Total Time: ", time() - start_time

# Completed on Fri, 7 Mar 2014, 02:41
# Correct answer: 986262, tried 986263, 986264
# Solve by:  6397
# ---------------
# 986263
# Total Time:  3757.72299981
# [Finished in 3757.9s]

# ========================================
# Other people's method
# ========================================
# max = 10**7
# count = 0
# div_count = [1] * max
# for d in xrange(2, max):
#     for i in xrange(d, max, d):
#         div_count[i] += 1

# for i in xrange(2, max-1):
#     if div_count[i] == div_count[i+1]:
#         count += 1

# print count

# 986262
# [Finished in 42.7s]
