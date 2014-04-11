# -*- coding: utf-8 -*-
# Problem 148
# Exploring Pascal's triangle

# We can easily verify that none of the entries in the first seven rows of
# Pascal's triangle are divisible by 7:
#                          1
#                      1       1
#                  1       2       1
#              1       3       3       1
#          1       4       6       4       1
#      1       5      10      10       5       1
# 1        6      15      20      15       6       1

# However, if we check the first one hundred rows, we will find that only 2361
# of the 5050 entries are not divisible by 7.

# Find the number of entries which are not divisible by 7 in the first one
# billion (10^9) rows of Pascal's triangle.

# 1. If n (the row number, starting with 0) is written in base 7, that is,
#    as a0*7⁰ + a1*7¹ + a2*7² + … + an*7^n, the number of non-divisibles in that
#    row is equal to (a0 + 1)*(a1 + 1)*(a2 + 1)* … *(an + 1). Example: take row
#    8992. In base 7, the number 8992 is represented as 35134. There are
#    therefore (3+1)*(5+1)*(1+1)*(3+1)*(4+1) = 960 non-divisibles by seven in
#    row 8992.

from time import time


def baseconvert(n, base):
    """
    convert positive decimal integer n to equivalent in another base (2-36)
    """
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    if n < 0 or base < 2 or base > 36:
        return ""

    s = ""
    while True:
        r = n % base
        s = digits[r] + s
        n = n / base
        if n == 0:
            break

    return s


# def non_divisibles(s):
#     digits = map(int, s)
#     count = 1
#     for d in digits:
#         count *= d + 1
#     return count

def non_divisibles(n):
    count = 1
    while n != 0:
        r = n % 10
        count *= r + 1
        n /= 10

    return count

start_time = time()

N = 1000000000
count = 0
for n in xrange(N):
    count += non_divisibles(int(baseconvert(n, 7)))

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Thu, 27 Mar 2014, 00:03
# Solve by: 
# ---------------
