# -*- coding: utf-8 -*-
# Problem 112
# Bouncy numbers

# Working from left-to-right if no digit is exceeded by the digit to its left it
# is called an increasing number; for example, 134468.

# Similarly if no digit is exceeded by the digit to its right it is called a
# decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor decreasing a
# "bouncy" number; for example, 155349.

# Clearly there cannot be any bouncy numbers below one-hundred, but just over
# half of the numbers below one-thousand (525) are bouncy. In fact, the least
# number for which the proportion of bouncy numbers first reaches 50% is 538.

# Surprisingly, bouncy numbers become more and more common and by the time we
# reach 21780 the proportion of bouncy numbers is equal to 90%.

# Find the least number for which the proportion of bouncy numbers is exactly
# 99%.

from time import time


def is_increasing(n):
    digits = list(str(n))
    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    return True


def is_decreasing(n):
    digits = list(str(n))
    for i in range(len(digits)-1):
        if digits[i+1] > digits[i]:
            return False
    return True

start_time = time()

n = 100
bouncing = 0

while bouncing < int(n * .99):
# while round(float(bouncing)/(n-1),4) < .99:   # Turns out this is not the same
    if not (is_increasing(n) or is_decreasing(n)):
        bouncing += 1

    n += 1

print bouncing
print n - 1
print round(float(bouncing)/(n-1),5)

print "Total Time: ", time() - start_time

# Completed on Thu, 6 Mar 2014, 03:22
# Solve by:  12778
# ---------------
# 1571130
# 1587000
# 0.99
# Total Time:  7.04600000381
# [Finished in 7.2s]
