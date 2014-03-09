# -*- coding: utf-8 -*-
# Problem 52
# Permuted multiples

# It can be seen that the number, 125874, and its double, 251748, contain exactly
# the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

from time import time

start_time = time()

x = 1
while True:
    l = [set(str(i * x)) for i in range(1, 7)]
    m = [l[0] == l[i] for i in range(len(l))]
    if all(m):
        print x
        break
    x += 1

print "Total Time: ", time() - start_time

# Completed on Wed, 5 Mar 2014, 20:44
# Solve by:  33868
# ---------------
# 142857
# Total Time:  1.35699987411
# [Finished in 1.5s]
