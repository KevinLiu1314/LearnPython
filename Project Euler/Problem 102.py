# -*- coding: utf-8 -*-
# Problem 102
# Triangle containment

# Three distinct points are plotted at random on a Cartesian plane, for which
# -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

# Consider the following two triangles:

# A(-340,495), B(-153,-910), C(835,-947)

# X(-175,41), Y(-421,-714), Z(574,-645)

# It can be verified that triangle ABC contains the origin, whereas triangle
# XYZ does not.

# Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text
# file containing the co-ordinates of one thousand "random" triangles, find
# the number of triangles for which the interior contains the origin.

# NOTE: The first two examples in the file represent the triangles in the
# example given above.

# 1. test to see if the area of ABC is equal to the area of the triangles
# 2. ABP + APC + PBC
# 3. http://en.wikipedia.org/wiki/Triangle#Using_coordinates gives the formula:
# 4. Area = 1/2|(Ax - Cx)(By - Ay) - (Ax - Bx)(Cy - Ay)|

from time import time


def area(A, B, C):
    """
    return double area of triangle ABC
    """

    return abs((A[0] - C[0]) * (B[1] - A[1]) - (A[0] - B[0]) * (C[1] - A[1]))

start_time = time()

count = 0
P = (0, 0)
for line in open("Problem 102.txt"):
    coordinates = map(int, line.strip().split(","))
    A = (coordinates[0], coordinates[1])
    B = (coordinates[2], coordinates[3])
    C = (coordinates[4], coordinates[5])
    if area(A, B, C) == area(A, B, P) + area(A, P, C) + area(P, B, C):
        count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Tue, 1 Apr 2014, 02:14
# Solve by: 11395
# ---------------
# Answer: 228
# Total Time:  0.0090000629425
# [Finished in 0.2s]
