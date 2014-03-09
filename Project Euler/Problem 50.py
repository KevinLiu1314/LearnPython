# -*- coding: utf-8 -*-
# Problem 50
# Consecutive prime sum

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

from time import time
from UsefulFunctions import primes, is_prime

start_time = time()

# Mothod 1, works for p < 100000, but impossible for p < 1000000
# Build the list of primes under 1000000
# pgen = primes()     # prime generator
# p = next(pgen)
# plist = []
# while p < 100000:
#     plist.append([p, 0])    # the prime number & terms
#     p = next(pgen)

# # Calculate longest consecutive terms for each prime number in the list
# for p in range(len(plist)):
#     # progress = int(float(p+1)/len(plist)*100)
#     # if progress % 10 == 0:
#     #     print progress, time() - start_time
#     i = 0
#     while True:
#         j = i
#         sum_ = plist[j][0]
#         terms = 1
#         while sum_ < plist[p][0]:
#             j += 1
#             terms += 1
#             sum_ += plist[j][0]
#             if terms > 547:
#                 print terms

#         if sum_ == plist[p][0]:
#             plist[p][1] = terms
#             break

#         i += 1

# print max(map(lambda p: p[1], plist))
# print "Total Time: ", time() - start_time

# Method 2, calculating intermediate sums with various lengths using different size sliding window
# We don't need all primes under 1000000, only those that summed together under 1000000
pgen = primes()     # prime generator
p = next(pgen)
plist = []
ubterms = 0     # upper bound of terms
sum_ = 0
while sum_ < 1000000:
    plist.append(p)
    ubterms += 1
    sum_ += p
    p = next(pgen)

print ubterms

# calculating all the possible sums
d = {}      # going to store a prime number & it's associated number of terms
for sliding_size in range(2, ubterms + 1):
    # calculate first window sum for new slice
    sum_ = 0
    for i in range(sliding_size):
        sum_ += plist[i]
    if sum_ % 2 != 0 and is_prime(sum_):
        d[sum_] = sliding_size

    # calculate sum for new window
    for i in range(1, ubterms - sliding_size):
        sum_ += plist[i + sliding_size - 1] - plist[i - 1]
        if sum_ % 2 != 0 and is_prime(sum_):
            d[sum_] = sliding_size

m = max(d.values())
for k in d:
    if d[k] == m:
        print "Total #: %d Prime #: %d has %d terms" % (len(d), k, d[k])

print "Total Time: ", time() - start_time

# Completed on Sat, 8 Mar 2014, 18:19
# Solve by:  29606
# ---------------
# 547
# Total #: 11082 Prime #: 997651 has 543 terms
# Total Time:  1.64199995995
# [Finished in 1.8s]
