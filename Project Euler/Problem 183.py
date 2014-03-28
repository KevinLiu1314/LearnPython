# -*- coding: utf-8 -*-
# Problem 183
# Maximum product of parts

# Let N be a positive integer and let N be split into k equal parts, r = N/k, so
# that N = r + r + ... + r.
# Let P be the product of these parts, P = r × r × ... × r = r^k.

# For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2
# + 2.2, then P = 2.2^5 = 51.53632.

# Let M(N) = Pmax for a given value of N.

# It turns out that the maximum for N = 11 is found by splitting eleven into
# four equal parts which leads to Pmax = (11/4)4; that is, M(11) = 14641/256 =
# 57.19140625, which is a terminating decimal.

# However, for N = 8 the maximum is achieved by splitting it into three equal
# parts, so M(8) = 512/27, which is a non-terminating decimal.

# Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a
# terminating decimal.

# For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.

# Find ΣD(N) for 5 ≤ N ≤ 10000.


def M(N):
    P = []
    for k in xrange(1, N + 1):
        p = k * math.log((float(N) / k))    # number too huge if (N/k)^k is used
        P.append((p, k))
    return max(P)


def is_terminal(n, d):
    """
    return True if n/d is terminal, False Otherwise
    """
    seen_before = []
    remainder = n % d
    while not remainder in seen_before:
        if remainder == 0:
            return True
        seen_before.append(remainder)
        remainder = remainder * 10 % d

    return False

from time import time
import math

start_time = time()

N = 10000

sum_ = 0
for n in xrange(5, N + 1):
    Pmax = M(n)
    if not is_terminal(n, Pmax[1]):
        sum_ += n
    else:
        sum_ -= n

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Fri, 28 Mar 2014, 01:00
# Solve by: 2800
# ---------------
# Answer: 48861552
# Total Time:  75.6029999256
# [Finished in 75.7s]
