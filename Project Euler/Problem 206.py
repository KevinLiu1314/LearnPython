# -*- coding: utf-8 -*-
# Problem 206
# Concealed Square

# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

# 1. The number has to be in the form 1_2_3_4_5_6_7_8_900.
# 2. Since only a number ending in 3 or 7 will give 9, we know it's an odd number
# 3. The maximum possible number is 19293949596979899, it's square root is
#    138902662, we'll use 138902663 and counting down by 2 to see if i^2 fits
#    the pattern


def match(n):
    pattern = "123456789"
    n_str = str(n)
    return all(pattern[i] == n_str[i * 2] for i in range(9))

from time import time

start_time = time()

n = 138902663
while not match(n ** 2):
    n -= 2

print "Answer:", n * 10

print "Total Time: ", time() - start_time

# Completed on Fri, 28 Mar 2014, 03:33
# Solve by: 11929
# ---------------
# Answer: 1389019170
# Total Time:  0.00499987602234
# [Finished in 0.1s]
