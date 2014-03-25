# -*- coding: utf-8 -*-
# Problem 69
# Totient maximum

# Euler's Totient function, φ(n) [sometimes called the phi function], is used to
# determine the number of numbers less than n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
# prime to nine, φ(9)=6.

# n   Relatively Prime    φ(n)    n/φ(n)
# 2   1                   1       2
# 3   1,2                 2       1.5
# 4   1,3                 2       2
# 5   1,2,3,4             4       1.25
# 6   1,5                 2       3
# 7   1,2,3,4,5,6         6       1.1666...
# 8   1,3,5,7             4       2
# 9   1,2,4,5,7,8         6       1.5
# 10  1,3,7,9             4       2.5

# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

from time import time
from UsefulFunctions import primes

start_time = time()

target = 1000000
numbers = [i - 1 for i in range(target + 1)]
pgen = primes()
p = next(pgen)
while p <= target / 2:
    for i in range(p, target + 1, p):
        numbers[i] -= numbers[i] / p
    p = next(pgen)

numbers[1] = 1  # get rid of the divide by zero error for special case
ratios = [(float(i) / numbers[i], i) for i in range(target + 1)]
print max(ratios)
print "Answer:", max(ratios)[1]

print "Total Time: ", time() - start_time

# Completed on Mon, 24 Mar 2014, 23:29
# Solve by: 17522
# ---------------
# (5.539388020833333, 510510)
# Answer: 510510
# Total Time:  4.1210000515
# [Finished in 4.8s]
