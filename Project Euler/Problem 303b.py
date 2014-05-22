# -*- coding: utf-8 -*-
# Problem 303
# Multiples with small digits

# For a positive integer n, define f(n) as the least positive multiple of n that,
# written in base 10, uses only digits ≤ 2.

# Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

# Also, sum f(n)/n for n from 1 to 100 =11363107

# Find sum f(n)/n for n from 1 to 10000

# f(9) = 12222
# f(99) = 1122222222
# f(999) = 111222222222222
# f(9999) = 11112222222222222222

sc = {9: 12222, 99: 1122222222, 999: 111222222222222, 9999: 11112222222222222222}  # special cases


def f(n):
    if n in sc:
        return sc[n] / n
    m = 1
    while True:
        p = n * m
        while p > 0:
            if p % 10 > 2:
                break
            p /= 10

        if p == 0:
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
# Solve by: 
# ---------------
# takes too long!