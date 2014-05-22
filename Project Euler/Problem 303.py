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
    #if n == 9999: return 11112222222222222222 # by 9, 99, 999 pattern
    while True:
        s = str(m * n)
        for idx in range(len(s)):
            if s[idx] not in ('0', '1', '2'): break
        else:
            return n * m
        mininc = 10**(len(s) - idx) - int(s[idx:])
        m += (mininc - 1)//n + 1

s = 0
for n in range(1, 10001): s += f(n) // n
print(s)

# Not solved
# Completed on Fri, 16 May 2014, 21:54
# Solve by: 1999
# ---------------
# 1111981904675169
# [Finished in 129.7s]
