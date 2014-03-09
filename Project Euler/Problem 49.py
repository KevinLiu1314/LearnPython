# -*- coding: utf-8 -*-
# Problem 49
# Prime permutations

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this
# sequence?

from time import time
from UsefulFunctions import primes, is_prime


# Assume the difference can be any number
# def is_the_one(first_term):
#     first_term_str = str(first_term)

#     for difference in range(1, 5000):    # to be conservative, 1000+5000+5000 will be > 9999
#         second_term = first_term + difference
#         second_term_str = str(second_term)
#         third_term = second_term + difference
#         third_term_str = str(third_term)

#         if len(first_term_str) != 4 or len(second_term_str) !=4 or len(third_term_str) != 4:
#             continue

#         if set(first_term_str) == set(second_term_str) == set(third_term_str) and is_prime(second_term) and is_prime(third_term):
#             return first_term_str + second_term_str + third_term_str

#     return False

# Assume the difference is 3330
def is_the_one(first_term):
    first_term_str = str(first_term)
    second_term = first_term + 3330
    second_term_str = str(second_term)
    third_term = second_term + 3330
    third_term_str = str(third_term)

    if set(first_term_str) == set(second_term_str) == set(third_term_str) and is_prime(second_term) and is_prime(third_term):
        return first_term_str + second_term_str + third_term_str
    else:
        return False


start_time = time()

# generate a list of all 4 digit prime numbers
pgen = primes()     # prime generator
p = next(pgen)
plist = []
while p < 10000:
    if p > 1000:
        plist.append(p)
    p = next(pgen)

i = 0
count = 0
while i < len(plist):
    if is_the_one(plist[i]):    # maybe True, or the concatenated number
        count += 1              # we need the 2nd one
        if count == 2:
            print is_the_one(plist[i])
            break
    i += 1

print "Total Time: ", time() - start_time

# Completed on Sat, 8 Mar 2014, 23:12
# Solve by:  27475
# ---------------
# 296962999629
# Total Time:  0.0139999389648
# [Finished in 0.2s]
