# -*- coding: utf-8 -*-
# Problem 28
# Number spiral diagonals

# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

from time import time


def m():
    direction = ["R", "D", "L", "U"]
    current_direction = 0
    steps = 1
    while True:
        for i in range(steps):
            yield direction[current_direction]

        current_direction = (current_direction + 1) % 4

        for i in range(steps):
            yield direction[current_direction]

        current_direction = (current_direction + 1) % 4

        steps += 1

start_time = time()

size = 1001
grid = [[0] * size for i in range(size)]
move = m()

i = j = size / 2
for n in range(1, size * size + 1):
    grid[i][j] = n
    direction = next(move)
    if direction == "R":
        j += 1
    elif direction == "D":
        i += 1
    elif direction == "L":
        j -= 1
    else:
        i -= 1

# for l in grid:
#     print l

sum = 0
for i in range(size):
    sum += grid[i][i] + grid[i][size - 1 - i]

# the center was counted twice
sum -= grid[size / 2][size / 2]
print sum

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 06:00
# Solve by: 55655
# ---------------
# 669171001
# Total Time:  0.664999961853
# [Finished in 0.9s]
