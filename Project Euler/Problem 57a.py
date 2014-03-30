# -*- coding: utf-8 -*-
# Problem 57
# Square root convergents

# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than denominator?

from time import time
from fractions import Fraction as F
    
start_time = time()

count = 0
for expansion in xrange(1000):
    i = expansion
    f = F(1, 2)
    while i != 0:
        f = F(2, 1) + f
        f = F(f.denominator, f.numerator)
        i -= 1
    f = F(1, 1) + f
    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Sat, 29 Mar 2014, 23:41
# Solve by:  20427
# ---------------
# Answer: 153
# Total Time:  121.334000111
# [Finished in 121.5s]
