# -*- coding: utf-8 -*-
# Problem 78
# Coin partitions

# Let p(n) represent the number of different ways in which n coins can be
# separated into piles. For example, five coins can separated into piles in
# exactly seven different ways, so p(5)=7.
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O

# Find the least value of n for which p(n) is divisible by one million.

# p(k) = p(k − 1) + p(k − 2) − p(k − 5) − p(k − 7) + p(k − 12) + p(k − 15) − p(k − 22) − ...
# http://en.wikipedia.org/wiki/Partition_%28number_theory%29#Generating_function
# http://en.wikipedia.org/wiki/Pentagonal_number

from time import time


def sign(n):
    if n % 4 < 2:
        return 1
    else:
        return -1

start_time = time()

p = [1]     # p(0)=1, by definition
n = 1
while True:
    i = 1
    gpn = 1     # generalized pentagonal numbers

    new_p = 0
    while gpn <= n:
        new_p += sign(i-1) * p[n-gpn]
        i += 1
        
        if i % 2 == 1:      # yielding the sequence 1, -1, 2, -2, 3, -3, etc.
            j = i / 2 + 1
        else:
            j = - i / 2
        
        gpn = (3*j**2-j)/2  # calculate the next generalized pentagonal numbers

    if new_p % 1000000 == 0:
        break

    p.append(new_p)
    n += 1

print new_p
print "Answer:", n

print "Total Time: ", time() - start_time

# Completed on Sat, 19 Apr 2014, 00:56
# Solve by: 8261
# ---------------
# Answer: 55374
# Total Time:  24.2369999886
# [Finished in 24.4s]
