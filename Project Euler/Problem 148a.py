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

from time import time


def next_row(row):
    """
    return the next row of Pascal's triangle
    """
    new_row = [1]
    for i in xrange(1, len(row)):
        new_row.append(row[i - 1] + row[i])
    new_row.append(1)

    return new_row

start_time = time()

N = 1000000000
count = 0
row = [1]
for n in xrange(N):
    for i in xrange(len(row)):
        if row[i] % 7 != 0:
            count += 1
    row = next_row(row)

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Thu, 27 Mar 2014, 00:03
# Solve by: 
# ---------------
# imposible to use brute force