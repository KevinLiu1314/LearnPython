# -*- coding: utf-8 -*-
# Problem 125
# Palindromic sums

# The palindromic number 595 is interesting because it can be written as the sum
# of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

# There are exactly eleven palindromes below one-thousand that can be written as
# consecutive square sums, and the sum of these palindromes is 4164. Note that
# 1 = 0^2 + 1^2 has not been included as this problem is concerned with the
# squares of positive integers.

# Find the sum of all the numbers less than 10^8 that are both palindromic and
# can be written as the sum of consecutive squares.

from time import time
import math


def is_palindromic(s):
    return s == s[::-1]

start_time = time()

# Generate squaers of numbers
N = 100000000
squares = [i**2 for i in xrange(1, int(math.sqrt(N))+1)]

palindromes = {}  # maybe duplicates
for i in xrange(len(squares) - 1):
    n = squares[i]
    for j in xrange(i + 1, len(squares)):
        n += squares[j]
        if n >= N:
            break
        if is_palindromic(str(n)):
            palindromes[n] = 1

print "Answer:", sum(palindromes)

print "Total Time: ", time() - start_time

# Completed on Wed, 30 Apr 2014, 01:34
# Solve by: 7507
# ---------------
# Answer: 2906969179
# Total Time:  0.344000101089
# [Finished in 0.5s]
