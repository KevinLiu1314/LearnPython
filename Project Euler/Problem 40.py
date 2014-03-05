# -*- coding: utf-8 -*-
# Problem 40
# Champernowne's constant

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the
# following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


from time import time

start_time = time()

d = ""
i = 1
while len(d) < 1000000:
    d += str(i)
    i += 1

l = [int(x) for x in (d[0], d[9], d[99], d[999], d[9999], d[99999], d[999999])]
print reduce(lambda x, y: x * y, l)

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 23:07
# Solve by: 39694
# ---------------
# 210
# Total Time:  0.231000185013
# [Finished in 0.4s]
