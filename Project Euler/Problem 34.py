# -*- coding: utf-8 -*-
# Problem 34
# Digit factorials

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math
from time import time

start_time = time()

d = {i: math.factorial(i) for i in range(10)}

l = []
n = 10
while True:
    digits = [int(x) for x in str(n)]
    sum = 0
    for digit in digits:
        sum += d[digit]

    if sum == n:
        l.append(n)

    n += 1

    print n

    if len(l) == 1: break

print l

print "Total Time: ", time() - start_time

