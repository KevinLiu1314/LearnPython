# -*- coding: utf-8 -*-
# Problem 119
# Digit power sum

# The number 512 is interesting because it is equal to the sum of its digits
# raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number
# with this property is 614656 = 284.

# We shall define an to be the nth term of this sequence and insist that a
# number must contain at least two digits to have a sum.

# You are given that a2 = 512 and a10 = 614656.

# Find a30.

from time import time
from math import *

def powersumgen():
    """ power sum generator """

    c = 10      # first candidate is 10
    while True:
        # digitsums = sum(map(int, list(str(c))))
        c_str = str(c)
        digitsums = 0
        for i in range(len(c_str)):
            digitsums += int(c_str[i])

        if digitsums == 1:  # special cases 10, 100, 1000 ect.
            c += 1
            continue

        power = int(log(c, digitsums))
        if c == digitsums ** power:
            yield c

        c += 1

start_time = time()

psg = powersumgen()

for i in range(30):
    print i + 1, next(psg)


print "Total Time: ", time() - start_time

# Completed on Thu, 6 Mar 2014, 03:22
# Solve by:  12778
# ---------------
