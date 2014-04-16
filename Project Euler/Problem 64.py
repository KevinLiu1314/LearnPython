# -*- coding: utf-8 -*-
# Problem 64
# Odd period square roots

# All square roots are periodic when written as continued fractions and can be
# written in the form:
# √N = a0 +   1
#     a1 +    1
#         a2 +    1
#             a3 + ...

# For example, let us consider √23:

# If we continue we would get the following expansion:

# The process can be summarised as follows:

# It can be seen that the sequence is repeating. For conciseness, we use the
# notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
# indefinitely.

# The first ten continued fraction representations of (irrational) square roots
# are:

# √2=[1;(2)], period=1
# √3=[1;(1,2)], period=2
# √5=[2;(4)], period=1
# √6=[2;(2,4)], period=2
# √7=[2;(1,1,1,4)], period=4
# √8=[2;(1,4)], period=2
# √10=[3;(6)], period=1
# √11=[3;(3,6)], period=2
# √12= [3;(2,6)], period=2
# √13=[3;(1,1,1,1,6)], period=5

# Exactly four continued fractions, for N ≤ 13, have an odd period.

# How many continued fractions for N ≤ 10000 have an odd period?

# 1. http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

from time import time
import math

start_time = time()

N = 10000
count = 0
S = 2
while S <= N:
    a0 = int(math.sqrt(S))
    if a0 ** 2 == S:        # skip the perfect squares
        S += 1
        continue
    period = 0
    m = 0
    d = 1
    a = a0
    while a != 2 * a0:
        new_m = d * a - m
        new_d = (S - new_m ** 2) / d
        new_a = int((a0 + new_m) / new_d)
        period += 1
        m, d, a = new_m, new_d, new_a
    
    if period % 2 == 1:
        count += 1

    S += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Tue, 15 Apr 2014, 02:33
# Solve by: 10947
# ---------------
# Answer: 1322
# Total Time:  0.350000143051
# [Finished in 0.5s]
