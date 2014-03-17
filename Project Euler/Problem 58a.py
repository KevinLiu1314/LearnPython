# -*- coding: utf-8 -*-
# Problem 58
# Spiral primes

# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued, what is the
# side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

from time import time
from UsefulFunctions import is_prime


def movegen():
    """
    1. short for "move generator"
    2. generate what the next direction will be in order to fill in a
       anticlockwise spiral N X N grid
    3. The sequence will look like this(5X5): RU LLDD RRRUUU LLLLDDDD RRRRR
    """
    direction = ["R", "U", "L", "D"]
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


def in_diagonal(i, j, size):
    """
    check to see if cell (i, j) lies in a diagonal of a "size" X "size" grid
    """
    if i == j:      # diagonal from upper left to lower right
        return True

    if j == size - 1 - i:   # diagonal from upper right to lower left
        return True

    return False


def build_grid(size):
    """
    1. build a "size" X "size" grid, and fill in the numbers
    2. keep track of "diagonal_primes" as we are filling in the numbers
    3. keep track of "diagonal_numbers" as we are filling in the numbers
    """
    #grid = [[0] * size for i in range(size)]
    move = movegen()

    diagonal_primes = 0
    diagonal_numbers = 0
    i = j = size / 2
    for n in range(1, size * size + 1):
        #grid[i][j] = n

        if in_diagonal(i, j, size):     # interesting things happening in the diagonal
            diagonal_numbers += 1
            if is_prime(n):
                diagonal_primes += 1

        direction = next(move)
        if direction == "R":
            j += 1
        elif direction == "D":
            i += 1
        elif direction == "L":
            j -= 1
        else:
            i -= 1

    return diagonal_primes, diagonal_numbers

start_time = time()

# 1. start with "side_len" = 7
# 2. build the "grid"
# 3. see if the primes/number ratio drop below 10%
# 3. if yes, print "side_len" and done
# 4. if not, increase "side_len" by 2 and repeat loop

side_len = 7
while True:
    diagonal_primes, diagonal_numbers = build_grid(side_len)
    #print "len: %d  primes: %d,  numbers: %d  percent: %f" % (side_len, diagonal_primes, diagonal_numbers, float(diagonal_primes)/diagonal_numbers)
    #print int(float(diagonal_primes)/diagonal_numbers*100)

    if int(float(diagonal_primes)/diagonal_numbers*100) < 10:
        print side_len
        break

    side_len += 2

print "Total Time: ", time() - start_time

# Completed on Tue, 11 Mar 2014, 00:56
# Solve by: 21290
# ---------------
