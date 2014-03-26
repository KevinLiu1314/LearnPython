# -*- coding: utf-8 -*-
# Problem 347
# Largest integer divisible by two primes

# The largest integer ≤ 100 that is only divisible by both the primes 2 and 3
# is 96, as 96=32*3=25*3. For two distinct primes p and q let M(p,q,N) be the
# largest positive integer ≤N only divisible by both p and q and M(p,q,N)=0 if
# such a positive integer does not exist.

# E.g. M(2,3,100)=96.
# M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
# Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that
# is divisible by both 2 and 73.

# Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

# Find S(10 000 000).

# 1. build a list from 0 to N with [0, 0, 0] -> [prime count, first prime, second prime]
# 2. for each prime under N/2, update each cell accordingly
# 3. put only the numbers with "prime count" == 2 into a dictionary
# 4. the sum of the values of the dictionary is the answer

from time import time
from UsefulFunctions import primes

start_time = time()

N = 10000000
numbers = [[0, 0, 0] for i in range(N + 1)]
pgen = primes()
p = next(pgen)
while p <= N / 2:
    for i in range(p, N + 1, p):
        numbers[i][0] += 1                  # new factor
        if numbers[i][0] <= 2:              # record the first & second prime only
            numbers[i][numbers[i][0]] = p
    p = next(pgen)

d = {}
for i in range(2, N + 1):
    if numbers[i][0] == 2:
        d[(numbers[i][1], numbers[i][2])] = i

print "Answer:", sum(d.values())

print "Total Time: ", time() - start_time

# Completed on Wed, 26 Mar 2014, 01:42
# Solve by: 1386
# ---------------
# Answer: 11109800204052
# Total Time:  108.404000044
# [Finished in 114.3s]
