# -*- coding: utf-8 -*-
# Problem 71
# Ordered fractions

# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that 2/5 is the fraction immediately to the left of 3/7.

# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
# order of size, find the numerator of the fraction immediately to the left of 3/7.

# 1. n/d < 3/7, solving for n gives n < 3/7 * d
# 2. for each d, calculate n and store F(n, d) in a list, excluding any F(3, 7)
# 3. the maximum of the list is the answer we want

from time import time
from fractions import Fraction as F
    
start_time = time()

reduced_proper_fractions = []

for d in xrange(2, 1000001):
    n = d * 3 / 7
    f = F(n, d)
    if f != F(3, 7):
        reduced_proper_fractions.append(f)

print max(reduced_proper_fractions)

print "Answer:", max(reduced_proper_fractions).numerator

print "Total Time: ", time() - start_time

# Completed on Sun, 30 Mar 2014, 00:36
# Solve by:  14714
# ---------------
# 428570/999997
# Answer: 428570
# Total Time:  19.3989999294
# [Finished in 19.8s]
