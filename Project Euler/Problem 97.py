# -*- coding: utf-8 -*-
# Problem 97
# Large non-Mersenne prime

# The first known prime found to exceed one million digits was discovered in
# 1999, and is a Mersenne prime of the form 2^6972593−1; it contains exactly
# 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1, have
# been found which contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which contains
# 2,357,207 digits: 28433×2^7830457+1.

# Find the last ten digits of this prime number.

from time import time

start_time = time()

p = 28433 * 2 ** 7830457 + 1

print str(p)[len(str(p)) - 10:]

print "Total Time: ", time() - start_time

# Completed on Thu, 6 Mar 2014, 00:49
# Solve by:  25508
# ---------------
# 8739992577
# Total Time:  921.742000103
# [Finished in 922.1s]
