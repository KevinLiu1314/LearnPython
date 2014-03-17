# -*- coding: utf-8 -*-
# Problem 100
# Arranged probability

# If a box contains twenty-one coloured discs, composed of fifteen blue discs
# and six red discs, and two discs were taken at random, it can be seen that the
# probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

# The next such arrangement, for which there is exactly 50% chance of taking two
# blue discs at random, is a box containing eighty-five blue discs and
# thirty-five red discs.

# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000
# discs in total, determine the number of blue discs that the box would contain.

# convert b/n * (b-1)/(n-1) = 1/2 to the diophantine equation:
# 2b^2 - 2b - n^2 + n = 0 and solve
# use the quadratic formula

from time import time

start_time = time()

b = 15
n = 21
target = 1000000000000
 
while n < target:
    newb = 3 * b + 2 * n - 2
    newn = 4 * b + 3 * n - 3
 
    b = newb
    n = newn

print "n: %d  b: %d" % (n, b)

print "Total Time: ", time() - start_time

# Completed on Sat, 15 Mar 2014, 22:11
# Solve by: 7815
# ---------------
# n: 1070379110497  b: 756872327473
# Total Time:  0.00399994850159
# [Finished in 0.2s]
