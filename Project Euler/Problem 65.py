# -*- coding: utf-8 -*-
# Problem 65
# Convergents of e

# The square root of 2 can be written as an infinite continued fraction.

# The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
# that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

# It turns out that the sequence of partial values of continued fractions for
# square roots provide the best rational approximations. Let us consider the
# convergents for √2.

# Hence the sequence of the first ten convergents for √2 are:
# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

from time import time
from fractions import Fraction as F

start_time = time()

terms = []            # we have 99 terms, plus the first term 2, total 100 terms
for i in xrange(1, 34):
    terms.append(1)
    terms.append(2 * i)
    terms.append(1)

i = 98                # the position of the term we want to expand
f = F(1, terms[i])
while i != 0:
    i -= 1
    f = F(terms[i], 1) + f
    f = F(f.denominator, f.numerator)

f = F(2, 1) + f

print "Answer:", sum(map(int, list(str(f.numerator))))

print "Total Time: ", time() - start_time

# Completed on Fri, 28 Mar 2014, 23:54
# Solve by: 15109
# ---------------
# Answer: 272
# Total Time:  0.00600004196167
# [Finished in 0.2s]
