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

from time import time

start_time = time()

def is_contain(x1, y1, x2, y2, x3, y3):
    allx = [x1, x2, x3]
    ally = [y1, y2, y3]
    x_all_negative = all(map(lambda x: x < 0, allx))
    x_all_positive = all(map(lambda x: x > 0, allx))
    y_all_negative = all(map(lambda y: y < 0, ally))
    y_all_positive = all(map(lambda y: y > 0, ally))
    
    if x_all_negative or x_all_positive:
        return False
    if y_all_negative or y_all_positive:
        return False

    return True
    
print "Total Time: ", time() - start_time

# Completed on Thu, 6 Mar 2014, 00:49
# Solve by:  25508
# ---------------
