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

# 1. start at first cell, set "path" to [(131, 0, 0)]
# 2. for each iteration, create a "new_paths" and loop through "paths"
#    check if there's a down path, if there is, sum it with current cell and add it to "new_paths"
#    check if there's a right path, if there is, sum it with current cell and add it to "new_paths"


def read_grid(filename):
    grid = []
    for line in open(filename):
        grid.append(map(int, line.strip().split(",")))
    return grid

from time import time

start_time = time()

grid = read_grid("Problem 81 5x5.txt")

paths = [(grid[0][0], 0, 0)]

for i in range((len(grid) - 1) * 2):
    new_paths = []
    for path in paths:
        if path[1] != len(grid) - 1:    # there's a down path
            sum_ = path[0] + grid[path[1] + 1][path[2]]
            new_paths.append((sum_, path[1] + 1, path[2]))
        if path[2] != len(grid) - 1:    # there's a right path
            sum_ = path[0] + grid[path[1]][path[2] + 1]
            new_paths.append((sum_, path[1], path[2] + 1))
    paths = new_paths

print min(paths)
print "Answer:", min(paths)[0]

print "Total Time: ", time() - start_time

# Completed on Sat, 15 Mar 2014, 22:11
# Solve by: 7815
# ---------------
