# -*- coding: utf-8 -*-
# Problem 68
# Magic 5-gon ring

# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
# each line adding to nine.

# Working clockwise, and starting from the group of three with the numerically
# lowest external node (4,3,2 in this example), each solution can be described
# uniquely. For example, the above solution can be described by the
# set: 4,3,2; 6,2,1; 5,1,3.

# It is possible to complete the ring with four different totals: 9, 10, 11, and
# 12. There are eight solutions in total.

# Total   Solution Set
# 9   4,2,3; 5,3,1; 6,1,2
# 9   4,3,2; 6,2,1; 5,1,3
# 10  2,3,5; 4,5,1; 6,1,3
# 10  2,5,3; 6,3,1; 4,1,5
# 11  1,4,6; 3,6,2; 5,2,4
# 11  1,6,4; 5,4,2; 3,2,6
# 12  1,5,6; 2,6,4; 3,4,5
# 12  1,6,5; 3,5,4; 2,4,6

# By concatenating each group it is possible to form 9-digit strings; the
# maximum string for a 3-gon ring is 432621513.

# Using the numbers 1 to 10, and depending on arrangements, it is possible to
# form 16- and 17-digit strings. What is the maximum 16-digit string for a
# "magic" 5-gon ring?

from time import time
import itertools


def same_sum(ring):
    """
    see if this current combination yield the same sum
    """
    sum_ = ring[0] + ring[1] + ring[2]
    for group in groups:
        if ring[group[0]] + ring[group[1]] + ring[group[2]] != sum_:
            return False
    return True


def digit_string(solution):
    """
    return "solution" in concatenated digits form, starts with lowest external node
    """
    external_nodes = []
    for i in xrange(5):
        external_nodes.append((solution[groups[i][0]], i))
    external_nodes = sorted(external_nodes)

    s = ""
    for i in xrange(external_nodes[0][1], 5):
        for j in groups[i]:
            s += str(solution[j])
    for i in xrange(0, external_nodes[0][1]):
        for j in groups[i]:
            s += str(solution[j])

    return s

start_time = time()

groups = [[0, 1, 2], [3, 2, 4], [5, 4, 6], [7, 6, 8], [9, 8, 1]]

solutions = []
for ring in itertools.permutations(range(1, 11)):
    if same_sum(ring):
        solutions.append(list(ring))

print sorted(solutions)

sixteen_digits = []
for solution in solutions:
    if len(digit_string(solution)) == 16:
        sixteen_digits.append(digit_string(solution))

print "Answer:", max(sixteen_digits)

print "Total Time: ", time() - start_time

# Completed on Wed, 16 Apr 2014, 22:53
# Solve by: 10264
# ---------------
# Answer: 6531031914842725
# Total Time:  3.44499993324
# [Finished in 3.6s]
