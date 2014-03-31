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
import math
    
start_time = time()

L = 1500000
bendables = {}          # "length":"ways", "length" that can be bend into a right triangle in "ways"
a = 3
while True:
    b = a + 1

    c = int(math.sqrt(a ** 2 + b ** 2))
    length = a + b + c
    if length > L:
        break

    while length <= L:
        if a ** 2 + b ** 2 == c ** 2:
            if length in bendables:
                bendables[length] += 1
            else:
                bendables[length] = 1
        b += 1
        c = int(math.sqrt(a ** 2 + b ** 2))
        length = a + b + c

    a += 1

count = 0
for length in bendables:
    if bendables[length] == 1:
        count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Sun, 30 Mar 2014, 04:51
# Solve by:  
# ---------------

# no answer, takes too long!
