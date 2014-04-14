# -*- coding: utf-8 -*-
# Problem 56
# Powerful digit sum

# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, what is the
# maximum digital sum?

from time import time

start_time = time()

numbers = [a ** b for a in range(100) for b in range(100)]
digits = [map(int, list(str(numbers[i]))) for i in range(len(numbers))]
digit_sums = map(sum, digits)
print max(digit_sums)

print "Total Time: ", time() - start_time

# Completed on Wed, 5 Mar 2014, 22:08
# Solve by:  29656
# ---------------
# 972
# Total Time:  0.446000099182
# [Finished in 0.6s]
