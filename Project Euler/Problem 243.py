# -*- coding: utf-8 -*-
# Problem 243
# Resilience

# A positive fraction whose numerator is less than its denominator is called a
# proper fraction.
# For any denominator, d, there will be d−1 proper fractions; for example, with
# d = 12:
# 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be the
# ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
# In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

from time import time

 
def answer():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    d = 1
    s = 1
    for p in primes:
        d *= p
        s *= p - 1
        for i in xrange(2, p):
            if float(s) * i / (d * i - 1) < 15499./94744:
                return d * i

start_time = time()

print "Answer:", answer()

print "Total Time: ", time() - start_time

# Completed on Sat, 29 Mar 2014, 04:37
# Solve by: 4743
# ---------------
# Answer: 892371480
# Total Time:  0.00300002098083
# [Finished in 0.2s]
