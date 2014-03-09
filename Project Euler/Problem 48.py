# -*- coding: utf-8 -*-
# Problem 48
# Self powers

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from time import time

start_time = time()

series = [i ** i for i in range(1, 1001)]
sum_str = str(sum(series))

print sum_str[len(sum_str) - 10:]

print "Total Time: ", time() - start_time

# Completed on Wed, 5 Mar 2014, 20:14
# Solve by:  60337
# ---------------
# 9110846700
# Total Time:  0.0420000553131
# [Finished in 0.2s]
