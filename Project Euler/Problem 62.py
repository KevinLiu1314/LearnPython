# -*- coding: utf-8 -*-
# Problem 62
# Cubic permutations

# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are
# cube.


from time import time

start_time = time()

d = {}
n = 1
while True:
    key = ''.join(sorted(list(str(n ** 3))))
    if key in d:
        if d[key][0] == 4:
            break
        else:
            d[key][0] += 1
    else:
        d[key] = [1, n ** 3]

    n += 1

print key, d[key]
print "Answer:", d[key][1]

print "Total Time: ", time() - start_time

# Completed on Sat, 12 Apr 2014, 04:44
# Solve by: 15328
# ---------------
# 012334556789 [4, 127035954683L]
# Answer: 127035954683
# Total Time:  0.0590000152588
# [Finished in 0.2s]
