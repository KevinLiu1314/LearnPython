# -*- coding: utf-8 -*-
# Problem 73
# Counting fractions in a range

# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 3 fractions between 1/3 and 1/2.

# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
# fractions for d ≤ 12,000?

# 1. n/d > 1/3 --> n > 1/3*d and n/d < 1/2 --> n < 1/2*d
# 2. for each d, calcualte min n and max n
# 3. loop through the range and count the # of reduced proper fractions

from time import time
from fractions import Fraction as F
    
start_time = time()

count = 0
for d in xrange(4, 12001):      # d = 1, 2, 3 won't be included in the count
    n_min = d / 3 + 1           # n must be at least this number
    n_max = d / 2
    if F(n_max, d) == F(1, 2):  # adjust for the case that n/d = 1/2 exactly
        n_max -= 1              # this adds up since we save 1 for every even #
    for n in xrange(n_min, n_max + 1):
        f = F(n, d)
        if f.denominator == d:
            count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Sun, 30 Mar 2014, 02:49
# Solve by:  13404
# ---------------
# Answer: 7295372
# Total Time:  74.5059998035
# [Finished in 74.7s]
