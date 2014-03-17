# -*- coding: utf-8 -*-
# Problem 99
# Largest exponential

# Comparing two numbers written in index form like 2^11 and 3^7 is not difficult,
# as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

# However, confirming that 632382^518061 > 519432^525806 would be much more
# difficult, as both numbers contain over three million digits.

# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
# containing one thousand lines with a base/exponent pair on each line,
# determine which line number has the greatest numerical value.

# NOTE: The first two lines in the file represent the numbers in the
# example given above.

from time import time
import math

start_time = time()

numbers = []
for line in open("Problem 99.txt"):
    pair = map(int, line.strip().split(","))
    numbers.append(pair[1] / math.log(10, pair[0]))

print "Maximum value at line #: ", numbers.index(max(numbers)) + 1

print "Total Time: ", time() - start_time

# Completed on Thu, 13 Mar 2014, 02:26
# Solve by: 15751
# ---------------
# Maximum value at line #:  709
# Total Time:  0.00600004196167
# [Finished in 0.2s]
