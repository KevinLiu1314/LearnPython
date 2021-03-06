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

# 1. http://en.wikipedia.org/wiki/Pythagorean_triple
# 2. The theory on Pythagorean triplets as given on Wikipedia states that we
#    can generate every primitive triplet by iterating over the integers m, n such
#    that m > n, and m+n is odd and gcd(n,m) ) 1 then the triplets are generated by
#    a = m^2 – n^2
#    b = 2mn
#    c = m^2 + n^2
# 3. c is the longest side, max c at m = n
# 4. m^2 + m^2 = c -> 2m^2 = 1500000 -> m = sqrt(150000/2)

from time import time
import math
import fractions


def primitive_triplets(limit):
    """
    returning all primitive triplets according to the formula for a, b, and c
    for m in the range 2 to "limit"
    """
    for m in xrange(2, limit + 1):
        for n in xrange(1, m):
            if (m + n) % 2 == 1 and fractions.gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                yield a, b, c

start_time = time()

L = 1500000
bendables = {}          # "length":"ways", "length" that can be bend into a right triangle in "ways"

for a, b, c in primitive_triplets(int(math.sqrt(L / 2))):
    primitive_triplets_length = a + b + c
    length = primitive_triplets_length
    while length <= L:              # multiples of the primitive triplet
        if length in bendables:
            bendables[length] += 1
        else:
            bendables[length] = 1
        length += primitive_triplets_length

count = 0
for length in bendables:
    if bendables[length] == 1:
        count += 1

print len(bendables)
print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Mon, 31 Mar 2014, 03:42
# Solve by: 8904
# ---------------
# 355571
# Answer: 161667
# Total Time:  2.0110001564
# [Finished in 2.3s]
