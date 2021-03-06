# -*- coding: utf-8 -*-
# Problem 86
# Cuboid route

# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and
# a fly, F, sits in the opposite corner. By travelling on the surfaces of the
# room the shortest "straight line" distance from S to F is 10 and the path is
# shown on the diagram.

# However, there are up to three "shortest" path candidates for any given cuboid
# and the shortest route doesn't always have integer length.

# By considering all cuboid rooms with integer dimensions, up to a maximum size
# of M by M by M, there are exactly 2060 cuboids for which the shortest route has
# integer length when M=100, and this is the least value of M for which the
# number of solutions first exceeds two thousand; the number of solutions is 1975
# when M=99.

# Find the least value of M such that the number of solutions first exceeds one
# million.

# 1. unfold the cuboid and the shortest path is:
# 2. s = sqrt(l^2 + (w+h)^2)

from time import time
import math

start_time = time()

count = 0
l = 3
while count <= 2000:
    for w in xrange(1, l+1):
        for h in xrange(1, l+1):
            s = math.sqrt(l**2 + (w+h)**2)
            if s == int(s):
                print l,w,h
                count += 1
    #break
    l += 1

print "Answer:", l, count

print "Total Time: ", time() - start_time

# Completed on Thu, 24 Apr 2014, 03:38
# Solve by: 
# ---------------
# not working