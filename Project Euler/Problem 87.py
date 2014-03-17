# -*- coding: utf-8 -*-
# Problem 87
# Prime power triples

# The smallest number expressible as the sum of a prime square, prime cube, and
# prime fourth power is 28. In fact, there are exactly four numbers below fifty
# that can be expressed in such a way:

# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4

# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?

from time import time
from UsefulFunctions import primes

start_time = time()

limit = 50000000
pgen = primes()     # prime generator
p = next(pgen)
p_square = []       # prime squares
p_cube = []         # prime cubes
p_four = []         # prime fourth power
while p ** 2 < limit:
    p_square.append(p ** 2)
    if p ** 3 < limit:
        p_cube.append(p ** 3)
        if p ** 4 < limit:
            p_four.append(p ** 4)
    p = next(pgen)


print "square: ", len(p_square), p_square[-1]
print "cube: ", len(p_cube), p_cube[-1]
print "four: ", len(p_four), p_four[-1]

d = {}      # holds the unique numbers
for first in p_square:
    for second in p_cube:
        for third in p_four:
            sum_ = first + second + third
            if sum_ < limit:
                if not sum_ in d:
                    d[sum_] = 1
                else:
                    d[sum_] += 1

print "Maximum Repeats: ", max(d.values())
print "Answer: ", len(d)

print "Total Time: ", time() - start_time

# Completed on Fri, 14 Mar 2014, 01:08
# Solve by: 10498
# ---------------
# square:  908 49970761
# cube:  73 49430863
# four:  23 47458321
# Maximum Repeats:  5
# Answer:  1097343
# Total Time:  1.85199999809
# [Finished in 2.2s]
