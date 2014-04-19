# -*- coding: utf-8 -*-
# Problem 78
# Coin partitions

# Let p(n) represent the number of different ways in which n coins can be
# separated into piles. For example, five coins can separated into piles in
# exactly seven different ways, so p(5)=7.
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O

# Find the least value of n for which p(n) is divisible by one million.

from time import time


def p(n):
    ways = [0] * (n + 1)
    ways[0] = 1

    for i in xrange(1, n + 1):
        for j in xrange(i, n + 1):
            ways[j] += ways[j - i]

    return ways[n]

start_time = time()

n = 2
while True:
    if p(n) % 1000000 == 0:
        break
    n += 1

print "Answer:", n

print "Total Time: ", time() - start_time

# Completed on Thu, 17 Apr 2014, 23:14
# Solve by: 
# ---------------
# too long!