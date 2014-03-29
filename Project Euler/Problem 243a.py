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
from fractions import Fraction as F


def R(n):
    proper_fractions = [F(i, n) for i in xrange(1, n)]
    resilient_count = 0
    for f in proper_fractions:
        if f.denominator == n:
            resilient_count += 1

    return F(resilient_count, n - 1)

start_time = time()

d = 2
while True:
    if R(d) < F(4, 10):
        break
    d += 1

print "Answer:", d

print "Total Time: ", time() - start_time

# works for d = 12, takes too much time
