# -*- coding: utf-8 -*-
# Problem 120
# Square remainders

# Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

# For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And
# as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

# For 3 ≤ a ≤ 1000, find ∑ rmax.

# 1. for even n's, the remainder is 2
# 2. for odd n's, the remainder is r=2an, 2an will always > 2
# 3. to maximized r, we need to find n that maximize 2an mod a^2
# 4. at 2an=multiples of a^2, the remainder is 0, n=a/2
# 5. to maximize 2an mod a^2, n=(a-1)/2
# 6. rmax = 2*a*((a-1)/2)

from time import time

start_time = time()

sum_ = 0
for a in xrange(3, 1001):
    sum_ += 2 * a * ((a - 1) / 2)

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Thu, 3 Apr 2014, 04:17
# Solve by: 7499
# ---------------
# Answer: 333082500
# Total Time:  0.00699996948242
# [Finished in 0.4s]
