# -*- coding: utf-8 -*-
# Problem 92
# Square digit chains

# A number chain is created by continuously adding the square of the digits in
# a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless
# loop. What is most amazing is that EVERY starting number will eventually arrive
# at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

from time import time


def new(n):
    s = 0
    for d in str(n):
        s += int(d) ** 2

    return s

start_time = time()

count = 0
i = 1
while i < 10000000:
    n = i
    while n != 1 and n != 89:
        # The below commented out code is elegant, but toooooo slow
        # n = sum(map(lambda x: x ** 2, map(int, list(str(n)))))
        n = new(n)

    if n == 89:     # check this terminating number
        count += 1

    i += 1

print count

print "Total Time: ", time() - start_time

# Completed on Thu, 6 Mar 2014, 00:13
# Solve by:  21318
# ---------------
# 8581146
# Total Time:  176.496000051
# [Finished in 176.7s]
