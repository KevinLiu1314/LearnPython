# -*- coding: utf-8 -*-
# Problem 82
# Path sum: three ways

# NOTE: This problem is a more challenging version of Problem 81.

# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
# the left column and finishing in any cell in the right column, and only moving
# up, down, and right, is indicated in red and bold; the sum is equal to 994.

# 131 673 234 103 18
# 201 96  342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37  331
    
# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
# As...'), a 31K text file containing a 80 by 80 matrix, from the left column to
# the right column.


def read_grid(filename):
    grid = []
    for line in open(filename):
        grid.append(map(int, line.strip().split(",")))
    return grid

from time import time

start_time = time()

grid = read_grid("Problem 82.txt")

grid_size = len(grid)
running_min = []
for i in xrange(grid_size):
    running_min.append(grid[i][grid_size-1])

for j in xrange(grid_size-2, -1, -1):
    # checking upward
    running_min[grid_size-1] += grid[grid_size-1][j]
    for i in xrange(grid_size-2, -1, -1):
        running_min[i] = min(running_min[i+1] + grid[i][j], running_min[i] + grid[i][j])

    # checking downward
    for i in xrange(1, grid_size):
        running_min[i] = min(running_min[i], running_min[i-1] + grid[i][j])

print "Answer:", min(running_min)

print "Total Time: ", time() - start_time

# Completed on Sun, 20 Apr 2014, 02:45
# Solve by: 10883
# ---------------
# Answer: 260324
# Total Time:  0.0149998664856
# [Finished in 0.2s]
