# -*- coding: utf-8 -*-
# Problem 187
# Semiprimes

# A composite is a number containing at least two prime factors. For example,
# 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

# There are ten composites below thirty containing precisely two, not
# necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# How many composite integers, n < 10^8, have precisely two, not necessarily
# distinct, prime factors?

from time import time
from UsefulFunctions import sieve

start_time = time()

N = 100000000
pnumbers = sieve(N / 2)      # list of prime numbers < N/2
print len(pnumbers)
print "Elapsed Time: ", time() - start_time

count = 0
i = 0
while pnumbers[i] ** 2 < N:
    j = i
    while pnumbers[i] * pnumbers[j] <= N:
        count += 1
        j += 1
        if j == len(pnumbers):
            break
    i += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Thu, 27 Mar 2014, 02:24
# Solve by: 6293
# ---------------
# 3001134
# Elapsed Time:  38.9450001717
# Answer: 17427258
# Total Time:  46.2950000763
# [Finished in 46.7s]
