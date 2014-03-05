# Problem 23
# Non-abundant sums

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
from time import time


def a(n):
    sum = 0
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            sum += i

    return sum > n


# Method 1 - took too long to run, may still be some logic error
def na(n):
    i = 0
    while n > a_nums[i]:
        difference = n - a_nums[i]
        if difference in a_nums:
            return False
        i += 1
        # if i == len(a_nums):
        #     return False

    return True


# get a list of all the abundant numbers
a_nums = []
for i in range(1, 28124):
    if a(i):
        a_nums.append(i)

t1 = time()

possible_list = {}
for i in a_nums:
    for j in a_nums:
        possible_list[i + j] = 1

# any nubmer not in the possible list will be included in the sum
na_nums = []
for i in range(1, 28124):
    if not i in possible_list:
        na_nums.append(i)

print na_nums

print sum(na_nums)

print time() - t1

# Completed on Mon, 3 Mar 2014, 03:49
# Solve by: 48221
# ---------------
# 4179871
# 10.0729999542
# [Finished in 25.3s]
