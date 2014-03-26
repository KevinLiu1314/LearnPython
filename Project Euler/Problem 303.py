# -*- coding: utf-8 -*-
# Problem 303
# Multiples with small digits

# For a positive integer n, define f(n) as the least positive multiple of n that,
# written in base 10, uses only digits ≤ 2.

# Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

# Also, sum f(n)/n for n from 1 to 100 =11363107

# Find sum f(n)/n for n from 1 to 10000


def f(n):
    m = 1
    while True:
        if set(str(m * n)) <= {'0', '1', '2'}:
            return m
        m += 1

from time import time

start_time = time()

N = 10000
sum_ = 0
for i in range(1, N + 1):
    sum_ += f(i)

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Wed, 26 Mar 2014, 01:42
# Solve by: 1386
# ---------------
# Answer: 11109800204052
# Total Time:  108.404000044
# [Finished in 114.3s]
