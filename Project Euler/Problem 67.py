# -*- coding: utf-8 -*-
# Problem 67
# Maximum path sum II

# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with
# one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible
# to try every route to solve this problem, as there are 2^99 altogether!
# If you could check one trillion (101^2) routes every second it would take over
# twenty billion years to check them all. There is an efficient algorithm to
# solve it. ;o)

from time import time

start_time = time()

# 1. Save the triangle into a 100 X 100 grid, we will have (0,0) to (99,99)
# 2. start from the 2nd to last row(98)
# 3. for each node in the row, add the current value to the max of next left and next right node
# 4. repeat this process until only the first row left
# 5. the total in (0, 0) is the max sum

# Save the triangle into a 100 X 100 grid
grid_size = 100
triangle = map(int, open("problem 67.txt").read().split())
grid = [[] for i in xrange(grid_size)]
i = 0       # index into the numbers in triangle
for j in xrange(grid_size):
    for k in xrange(j + 1):
        grid[j].append(triangle[i])
        i += 1

# start from the 2nd to last row
i = grid_size - 2
while i >= 0:
    for j in range(i + 1):
        grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])
    i -= 1

print grid[0][0]

print "Total Time: ", time() - start_time

# Completed on Mon, 10 Mar 2014, 23:36
# Solve by: 50038
# ---------------
# 7273
# Total Time:  0.010999917984
# [Finished in 0.1s]
