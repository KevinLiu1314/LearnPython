# -*- coding: utf-8 -*-
# Problem 81
# Path sum: two ways

# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is indicated in bold red
# and is equal to 2427.

# 131 673 234 103 18
# 201 96  342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37  331

# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
# As...'), a 31K text file containing a 80 by 80 matrix, from the top left to
#  the bottom right by only moving right and down.

# 1. initialize "sums[0][0]" to grid[0][0]
# 2. loop through each cell in "sums" using i,j as indexes
# 3. record the min sum at sums[i][j]
# 4. the answer is in the last cell of "sums"

def read_grid(filename):
    grid = []
    for line in open(filename):
        grid.append(map(int, line.strip().split(",")))
    return grid

from time import time

start_time = time()

grid = read_grid("Problem 81.txt")

sums = [[0] * len(grid) for i in range(len(grid))]
sums[0][0] = grid[0][0]

for i in range(len(grid)):
    for j in range(len(grid)):
        if i == 0 and j == 0:   # just starting
            continue
        if i == 0:  # first row
            sums[i][j] = grid[i][j] + sums[i][j - 1]
            continue
        if j == 0:  # first column
            sums[i][j] = grid[i][j] + sums[i - 1][j]
            continue
        sums[i][j] = grid[i][j] + min(sums[i][j - 1], sums[i - 1][j])

print "Answer:", sums[len(grid) - 1][len(grid) - 1]

print "Total Time: ", time() - start_time

# Completed on Sat, 22 Mar 2014, 05:12
# Solve by: 17841
# ---------------
# Answer: 427337
# Total Time:  0.0249998569489
# [Finished in 0.3s]
