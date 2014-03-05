# -*- coding: utf-8 -*-
# Problem 36
# Double-base palindromes

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

from time import time
from UsefulFunctions import palindromic

start_time = time()

l = []
i = 1
while i < 1000000:
    if palindromic(str(i)) and palindromic(str(bin(i))[2:]):
        l.append(i)
    i += 1

print l
print sum(l)

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 21:32
# Solve by: 45334
# ---------------
# [1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585]
# 872187
# Total Time:  2.20699977875
# [Finished in 2.4s]
