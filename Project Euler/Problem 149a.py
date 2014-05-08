# -*- coding: utf-8 -*-
# Problem 149
# Searching for a maximum-sum subsequence

# Looking at the table below, it is easy to verify that the maximum possible sum
# of adjacent numbers in any direction (horizontal, vertical, diagonal or
# anti-diagonal) is 16 (= 8 + 7 + 1).
# −2  5   3   2
#  9 −6   5   1
#  3  2   7   3
# −1  8  −4   8

# Now, let us repeat the search, but on a much larger scale:

# First, generate four million pseudo-random numbers using a specific form of
# what is known as a "Lagged Fibonacci Generator":

# For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k^3] (modulo 1000000) − 500000.
# For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.

# Thus, s10 = −393027 and s100 = 86613.

# The terms of s are then arranged in a 2000×2000 table, using the first 2000
# numbers to fill the first row (sequentially), the next 2000 numbers to fill
# the second row, and so on.

# Finally, find the greatest sum of (any number of) adjacent entries in any
# direction (horizontal, vertical, diagonal or anti-diagonal).

from time import time


def maximum(l):
    """
    return the greatest sum of any number of adjacent entries in "l"
    """
    if len(l) == 1:
        return l[0]
    max_ = 0
    for i in xrange(len(l) - 1):
        m = l[i]
        if m > max_:
            max_ = m
        for j in xrange(i + 1, len(l)):
            m += l[j]
            if m > max_:
                max_ = m
    return max_

start_time = time()

s = [0]
for k in xrange(1, 56):
    sk = (100003 - 200003*k + 300007*(k**3)) % 1000000 - 500000
    s.append(sk)

for k in xrange(56, 4000001):
    sk = (s[k-24] + s[k-55] + 1000000) % 1000000 - 500000
    s.append(sk)

# s = [0, -2, 5, 3, 2, 9, -6, 5, 1, 3, 2, 7, 3, -1, 8, -4, 8]
grid = []
N = 2000
for i in xrange(N):
    row = []
    for j in xrange(N):
        row.append(s[i * N + j + 1])
    grid.append(row)

max_ = 0
# horizontal
for i in xrange(N):
    l = []
    for j in xrange(N):
        l.append(grid[i][j])
    m = maximum(l)
    if m > max_:
        max_ = m

# vertical
for j in xrange(N):
    l = []
    for i in xrange(N):
        l.append(grid[i][j])
    m = maximum(l)
    if m > max_:
        max_ = m

# diagonal
for k in xrange(N):
    l = []
    i = 0
    j = k
    c = 0
    while c <= k:
        l.append(grid[i][j])
        i += 1
        j -= 1
        c += 1
    m = maximum(l)
    if m > max_:
        max_ = m
for k in xrange(N - 1):
    l = []
    i = N - 1 - k
    j = N - 1
    c = 0
    while c <= k:
        l.append(grid[i][j])
        i += 1
        j -= 1
        c += 1
    m = maximum(l)
    if m > max_:
        max_ = m

# anti diagonal
for k in xrange(N):
    l = []
    i = 0
    j = N - 1 - k
    c = 0
    while c <= k:
        l.append(grid[i][j])
        i += 1
        j += 1
        c += 1
    m = maximum(l)
    if m > max_:
        max_ = m
for k in xrange(N - 1):
    l = []
    i = N - 1 - k
    j = 0
    c = 0
    while c <= k:
        l.append(grid[i][j])
        i += 1
        j += 1
        c += 1
    m = maximum(l)
    if m > max_:
        max_ = m

print "Answer:", max_

print "Total Time: ", time() - start_time

# Completed on Thu, 8 May 2014, 01:56
# Solve by: 2602
# ---------------
# Answer: 52852124
# Total Time:  2400.26999998
# [Finished in 2400.6s]
