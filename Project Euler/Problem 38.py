# -*- coding: utf-8 -*-
# Problem 38
# Pandigital multiples

# Take the number 192 and multiply it by each of 1, 2, and 3:

#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product of
# 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

from time import time


def cp(i, n):
    """
    return the concatenated product of i and n
    """
    cp_str = ""
    for j in range(1, n + 1):
        cp_str += str(i * j)

    return cp_str


def is_pandigital(n_str):
    """
    expects a number string
    """
    return set(str(i) for i in range(1, len(n_str) + 1)) == set(n_str)

start_time = time()

# start with i = 1, varies n until we have a 9 digit concatenated product,
# put this product into the dictionary d as key, (i, n) as value
# keep only keys that are pandigital
# find the max key in the dictionary d
d = {}
i = 1   # this is the integer
while True:
    n = 2
    
    # skip all cp that have len < 9
    new_cp = cp(i, n)
    while len(new_cp) < 9:
        n += 1
        new_cp = cp(i, n)
        
    # keep only cp that have len == 9
    while len(new_cp) == 9:
        d[new_cp] = (i, n)
        n += 1
        new_cp = cp(i, n)

    # n becomes too big
    if n == 2:
        break

    i += 1

# filter out only keys that are pandigital into the p(pandigital) list
p = filter(is_pandigital, d)

print max(p)
print d[max(p)]

print "Total Time: ", time() - start_time

# Completed on Sun, 9 Mar 2014, 01:24
# Solve by: 30623
# ---------------
# 932718654
# (9327, 2)
# Total Time:  0.0729999542236
# [Finished in 0.2s]
