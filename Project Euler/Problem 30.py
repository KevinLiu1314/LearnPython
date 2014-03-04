# -*- coding: utf-8 -*-
# ProblemA 30
# Digit fifth powers

# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:

#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 4^4

# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.


def sum_is_equal_to_power(n):
    powers = map(lambda x: int(x) ** 5, list(str(n)))
    return sum(powers) == n

from time import time

start_time = time()

l = []
for i in range(2, 1000000):
    if sum_is_equal_to_power(i):
        l.append(i)

print l
print sum(l)

print "Total Time: ", time() - start_time

# [4150, 4151, 54748, 92727, 93084, 194979]
# 443839
# Total Time:  6.39100003242
# [Finished in 6.6s]

# Other answers
# b=[]
# for a in range(2,1000000):
#     if a==sum([int(str(a)[x])**5 for x in range(0,len(str(a)))]):
#         b.append(a)
# print b
# print sum(b)
