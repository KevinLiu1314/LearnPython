# -*- coding: utf-8 -*-
# Problem 148
# Exploring Pascal's triangle

# We can easily verify that none of the entries in the first seven rows of
# Pascal's triangle are divisible by 7:
#                          1
#                      1       1
#                  1       2       1
#              1       3       3       1
#          1       4       6       4       1
#      1       5      10      10       5       1
# 1        6      15      20      15       6       1

# However, if we check the first one hundred rows, we will find that only 2361
# of the 5050 entries are not divisible by 7.

# Find the number of entries which are not divisible by 7 in the first one
# billion (10^9) rows of Pascal's triangle.

# 1. If n (the row number, starting with 0) is written in base 7, that is,
#    as a0*7⁰ + a1*7¹ + a2*7² + … + an*7^n, the number of non-divisibles in that
#    row is equal to (a0 + 1)*(a1 + 1)*(a2 + 1)* … *(an + 1). Example: take row
#    8992. In base 7, the number 8992 is represented as 35134. There are
#    therefore (3+1)*(5+1)*(1+1)*(3+1)*(4+1) = 960 non-divisibles by seven in
#    row 8992.

from time import time

start_time = time()

N = 1000000000
count = 0
for n in xrange(N):
    non_divisibles = 1
    while n != 0:
        r = n % 7
        non_divisibles *= r + 1
        n /= 7
    count += non_divisibles

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Thu, 3 Apr 2014, 01:12
# Solve by: 2786
# ---------------
# Answer: 2129970655314432
# Total Time:  4812.78499985
# [Finished in 4812.9s]
