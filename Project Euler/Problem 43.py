# -*- coding: utf-8 -*-
# Problem 43
# Sub-string divisibility

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:

#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations


def pandigitals():
    for n in permutations([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]):
        if n[0] == 0:
            break
        yield n

from time import time

start_time = time()

p_list = [2, 3, 5, 7, 11, 13, 17]
l = []
p = pandigitals()
while True:
    try:
        raw_n = next(p)
    except:
        break
    sub_n = [raw_n[i]*100+raw_n[i+1]*10+raw_n[i+2] for i in range(1, 8)]
    if all(sub_n[i] % p_list[i] == 0 for i in range(7)):
        l.append(reduce(lambda x, y: 10 * x + y, raw_n))

print l
print sum(l)

print "Total Time: ", time() - start_time

# Completed on Wed, 5 Mar 2014, 01:20
# Solve by: 28109
# ---------------
# [4160357289L, 4130952867L, 4106357289L, 1460357289, 1430952867, 1406357289]
# 16695334890
# Total Time:  20.7949998379
# [Finished in 21.0s]
