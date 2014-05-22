# -*- coding: utf-8 -*-
# Problem 159
# Digital root sums of factorisations

# A composite number can be factored many different ways. For instance, not
# including multiplication by one, 24 can be factored in 7 distinct ways:
# 24 = 2x2x2x3
# 24 = 2x3x4
# 24 = 2x2x6
# 24 = 4x6
# 24 = 3x8
# 24 = 2x12
# 24 = 24

# Recall that the digital root of a number, in base 10, is found by adding
# together the digits of that number, and repeating that process until a number
# is arrived at that is less than 10. Thus the digital root of 467 is 8.

# We shall call a Digital Root Sum (DRS) the sum of the digital roots of the
# individual factors of our number.
# The chart below demonstrates all of the DRS values for 24.
# Factorisation   Digital Root Sum
# 2x2x2x3         9
# 2x3x4           9
# 2x2x6           10
# 4x6             10
# 3x8             11
# 2x12            5
# 24              6

# The maximum Digital Root Sum of 24 is 11.
# The function mdrs(n) gives the maximum Digital Root Sum of n. So mdrs(24)=11.
# Find ∑mdrs(n) for 1 < n < 1,000,000.

# The digital root sum of positive integer n, drs(n), is given by
# drs(n) = n - int((n-1)/9)*9
# The maximum digital root sum of a factorization of n is given by
# mdrs(p) = drs(p) if p is prime mdrs(n) = max(mdrs(a)+mdrs(b)) for all ab=n)

from time import time

start_time = time()

mdrs = [0] * 1000000
for i in range(2, 1000000):
    mdrs[i] = i - int((i - 1) / 9) * 9

for i in range(2, 1000000):
    j = 2
    while i * j < 1000000 and j <= i:
        mdrs[i * j] = max(mdrs[i * j], mdrs[i] + mdrs[j])
        j += 1

sum_ = 0
for i in range(2, 1000000):
    sum_ += mdrs[i]


print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Wed, 14 May 2014, 00:09
# Solve by: 1825
# ---------------
# Answer: 14489159
# Total Time:  5.40300011635
# [Finished in 5.5s]
