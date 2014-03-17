# -*- coding: utf-8 -*-
# Problem 85
# Counting rectangles

# By counting carefully it can be seen that a rectangular grid measuring 3 by 2
# contains eighteen rectangles:

# Although there exists no rectangular grid that contains exactly two million
# rectangles, find the area of the grid with the nearest solution.


def rect_in_width(w):
    count = 0
    for width_size in range(1, w + 1):
            count += w + 1 - width_size
    return count


# def rect_count(l, w):
#     count = 0
#     for length_size in range(1, l + 1):
#             count += l + 1 - length_size
    
#     return count * rect_in_width(w)


def rect_count(l, w):
    return (1+l)*l/2 * (1+w)*w/2

from time import time

start_time = time()

limit = 2000000
d = {}      # dictionary holds (l, w) & rectangle counts
l = 1
while True:
    w = 1
    rectangles = rect_count(l, w)
    if rectangles >= limit:
        if not ((l, w) in d or (w, l) in d):
            d[(l, w)] = rectangles  # over shoot by 1 just to be safe
        break

    while rectangles < limit:
        if not ((l, w) in d or (w, l) in d):
            d[(l, w)] = rectangles
        w += 1
        rectangles = rect_count(l, w)

    if not ((l, w) in d or (w, l) in d):
        d[(l, w)] = rectangles  # over shoot by 1 just to be safe

    l += 1

nearest = []
for k in d:
    nearest.append((abs(limit - d[k]), d[k], k))
print sorted(nearest)[:3]

print "Answer: ", sorted(nearest)[0][2][0] * sorted(nearest)[0][2][1]

print "Total Time: ", time() - start_time

# Completed on Fri, 14 Mar 2014, 03:44
# Solve by: 12701
# ---------------
# [(2, 1999998, (36, 77)), (16, 2000016, (3, 816)), (16, 2000016, (16, 171))]
# Answer:  2772
# Total Time:  1.27399992943
# [Finished in 1.4s]
