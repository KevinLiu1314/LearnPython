# -*- coding: utf-8 -*-
# Problem 31
# Coin sums

# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?


from time import time

start_time = time()

n = 200
ways = 0
for c1 in range(n / 200 + 1):
    for c2 in range(n / 100 + 1):
        if c1 * 200 > n: break
        for c3 in range(n / 50 + 1):
            if c1 * 200 + c2 * 100 > n: break
            for c4 in range(n / 20 + 1):
                if c1 * 200 + c2 * 100 + c3 * 50 > n: break
                for c5 in range(n / 10 + 1):
                    if c1 * 200 + c2 * 100 + c3 * 50 + c4 * 20 > n: break
                    for c6 in range(n / 5 + 1):
                        if c1 * 200 + c2 * 100 + c3 * 50 + c4 * 20 + c5 * 10 > n: break
                        for c7 in range(n / 2 + 1):
                            if c1 * 200 + c2 * 100 + c3 * 50 + c4 * 20 + c5 * 10 + c6 * 5 > n: break
                            for c8 in range(n + 1):
                                if c1 * 200 + c2 * 100 + c3 * 50 + c4 * 20 + c5 * 10 + c6 * 5 + c7 * 2 > n: break
                                if c1 * 200 + c2 * 100 + c3 * 50 + c4 * 20 + c5 * 10 + c6 * 5 + c7 * 2 + c8 == n:
                                    ways += 1
                                    break       # adding a break here takes off 10 seconds

print ways

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 16:11
# Solve by: 39270
# ---------------
# 73682
# Total Time:  3.59500002861
# [Finished in 3.8s]
