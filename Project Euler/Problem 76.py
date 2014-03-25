# -*- coding: utf-8 -*-
# Problem 76
# Counting summations

# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two
# positive integers?


def combinations(number, target):
    """
    return the number of combinations "target" can be achieved with "number" of numbers
    1. build a "nubmers" list, "count - 1" long, that will hold the combinations, filled with 1s initially
    2. use "index" to keep track of the position of the last varying number
    """
    numbers = [1 for i in range(number - 1)]
    index = number - 2
    count = 0

    sum_so_far = sum(numbers)
    difference = target - sum_so_far
    while True:
        if difference >= numbers[index]:
            count += (difference - numbers[index]) / 2 + 1

        index -= 1
        if index < 0:
            break
        numbers[index] += 1
        for i in range(index + 1, len(numbers)):
            numbers[i] = numbers[index]

        sum_so_far = sum(numbers)
        difference = target - sum_so_far
        if difference >= numbers[-1]:
            index = number - 2

    return count

from time import time

start_time = time()

target = 100
count = 0
for i in range(2, target + 1):
    count += combinations(i, target)

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Mon, 24 Mar 2014, 03:23
# Solve by: 14777
# ---------------
# Answer: 190569291
# Total Time:  107.255000114
# [Finished in 107.4s]
