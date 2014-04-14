# -*- coding: utf-8 -*-
# Problem 63
# Powerful digit counts

# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?


from time import time

start_time = time()

count = 0
n = 1
while 10**(n-1) < 9**n:
    for x in xrange(1, 10):
        if x**n >= 10**(n-1):
            count += 1
    n += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Sat, 12 Apr 2014, 17:21
# Solve by: 22029
# ---------------
# Answer: 49
# Total Time:  0.0019998550415
# [Finished in 0.1s]
