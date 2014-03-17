# Problem 26
# Reciprocal cycles

# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit raw_fractions with denominators 2 to 10 are given:

#     1/2 =   0.5
#     1/3 =   0.(3)
#     1/4 =   0.25
#     1/5 =   0.2
#     1/6 =   0.1(6)
#     1/7 =   0.(142857)
#     1/8 =   0.125
#     1/9 =   0.(1)
#     1/10    =   0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.

import itertools
from time import time


def repeat_len(n):
    """
    returns the repeating len when 1 is divided by n
    Algorithm: remember the position of each remainder, find the next remainder until
      (1) remainder == 0: 1 can be evenly divided by n, repeat len = 0
      (2) remainder is seen before: repeating len is current position - remembered position
    """
    seen = {}
    r = 10      # initially we have 1/n, quotient is 0, we then multiply 1 by 10
    for i in itertools.count():
        r = r % n
        if r == 0:
            return 0
        if r in seen:
            return i - seen[r]
        seen[r] = i
        r *= 10

start_time = time()

l = [(repeat_len(d), d) for d in range(1, 1000)]
print "len: %d, d: %d " % max(l)

print "Total Time: ", time() - start_time


# Completed on Sun, 9 Mar 2014, 23:53
# Solve by: 39715
# ---------------
# len: 982, d: 983 
# Total Time:  0.0360000133514
# [Finished in 0.2s]
