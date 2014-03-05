# Problem 24
# Lexicographic permutations

# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations


def p(digits):
    for n in sorted(permutations(digits)):
        yield n

perm = p([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
i = 1
while i <= 1000000:
    number = next(perm)
    i += 1

print reduce(lambda x, y: str(x) + str(y), number)

# Completed on Tue, 4 Mar 2014, 18:44
# Solve by: 55624
# ---------------
# 2783915460
# [Finished in 0.6s]
