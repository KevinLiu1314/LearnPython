# -*- coding: utf-8 -*-
# Problem 74
# Digit factorial chains

# The number 145 is well known for the property that the sum of the factorial of
# its digits is equal to 145:

# 1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the longest chain of
# numbers that link back to 169; it turns out that there are only three such
# loops that exist:

# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872

# It is not difficult to prove that EVERY starting number will eventually get
# stuck in a loop. For example,

# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)

# Starting with 69 produces a chain of five non-repeating terms, but the longest
# non-repeating chain with a starting number below one million is sixty terms.

# How many chains, with a starting number below one million, contain exactly
# sixty non-repeating terms?

from time import time
import math
    
start_time = time()

factorials = {i: math.factorial(i) for i in range(0, 10)}

count = 0
for n in xrange(1, 1000000):
    term = n
    chain_len = 0
    seen_before = []
    while not term in seen_before:
        chain_len += 1
        seen_before.append(term)
        newterm = 0
        while term > 0:
            remainder = term % 10
            newterm += factorials[remainder]
            term /= 10
        term = newterm
    if chain_len == 60:
        count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Sun, 30 Mar 2014, 04:51
# Solve by:  13611
# ---------------
# Answer: 402
# Total Time:  75.0529999733
# [Finished in 75.2s]
