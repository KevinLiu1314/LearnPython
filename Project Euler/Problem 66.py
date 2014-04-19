# -*- coding: utf-8 -*-
# Problem 66
# Diophantine equation

# Consider quadratic Diophantine equations of the form:

# x^2 – Dy^2 = 1

# For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

# It can be assumed that there are no solutions in positive integers when D is
# square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
# following:

# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
# obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest
# value of x is obtained.

# 1. http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Pell.27s_equation

from time import time
import math
from fractions import Fraction as F


def convergent(terms):
    """
    return the convergent of the continue fraction expansion
    """
    i = len(terms) - 1           # expand from last term
    if i == 0:
        return F(terms[0], 1)

    f = F(1, terms[i])
    while i != 1:
        i -= 1
        f = F(terms[i], 1) + f
        f = F(f.denominator, f.numerator)

    return F(terms[0], 1) + f

start_time = time()

D = 2
x = {}
while D <= 1000:
    a0 = int(math.sqrt(D))
    if a0 ** 2 == D:        # skip the perfect squares
        D += 1
        continue
    m = 0
    d = 1
    a = a0
    terms = [a]
    num = convergent(terms).numerator
    den = convergent(terms).denominator
    while num * num - D * den * den != 1:
        new_m = d * a - m
        new_d = (D - new_m ** 2) / d
        new_a = int((a0 + new_m) / new_d)
        m, d, a = new_m, new_d, new_a
        terms.append(a)
        num = convergent(terms).numerator
        den = convergent(terms).denominator

    x[D] = num
    D += 1

max_x = max(x.values())
for d in x:
    if x[d] == max_x:
        print "D: %d, x: %d" % (d, x[d])
        break

print "Total Time: ", time() - start_time

# Completed on Wed, 16 Apr 2014, 02:56
# Solve by: 9693
# ---------------
# D: 661, x: 16421658242965910275055840472270471049
# Total Time:  7.01800012589
# [Finished in 7.2s]
