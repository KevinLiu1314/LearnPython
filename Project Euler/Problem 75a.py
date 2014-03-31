# -*- coding: utf-8 -*-
# Problem 75
# Singular integer right triangles

# It turns out that 12 cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there are
# many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
# integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 cm it is possible to form exactly
# three different integer sided right angle triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values of L ≤ 1,500,000
# can exactly one integer sided right angle triangle be formed?

from time import time
    

def ways(l):
    """
    return how many ways a length of "l" can be bend into a right triangle
    with sides a, b, and c
    """
    count = 0
    a = 1
    while True:
        b = a + 1
        c = l - a - b

        if a ** 2 + b ** 2 > c ** 2:
            return count

        while a ** 2 + b ** 2 < c ** 2:
            b += 1
            c = l - a - b

        if a ** 2 + b ** 2 == c ** 2:
            count += 1

        a += 1

start_time = time()

L = 1500000
count = 0

for i in xrange(12, L + 1):
    if ways(i) == 1:
        count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Sun, 30 Mar 2014, 04:51
# Solve by:  
# ---------------

# no answer, takes too long!
