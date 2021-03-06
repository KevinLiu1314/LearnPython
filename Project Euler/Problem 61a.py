# -*- coding: utf-8 -*-
# Problem 61
# Cyclical figurate numbers

# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
# all figurate (polygonal) numbers and are generated by the following formulae:
# Triangle        P3,n=n(n+1)/2       1, 3, 6, 10, 15, ...
# Square          P4,n=n^2            1, 4, 9, 16, 25, ...
# Pentagonal      P5,n=n(3n−1)/2      1, 5, 12, 22, 35, ...
# Hexagonal       P6,n=n(2n−1)        1, 6, 15, 28, 45, ...
# Heptagonal      P7,n=n(5n−3)/2      1, 7, 18, 34, 55, ...
# Octagonal       P8,n=n(3n−2)        1, 8, 21, 40, 65, ...

# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
# interesting properties.

#     The set is cyclic, in that the last two digits of each number is the first
#     two digits of the next number (including the last number with the first).
#     Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and
#     pentagonal (P5,44=2882), is represented by a different number in the set.
#     This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which
# each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
# octagonal, is represented by a different number in the set.


def get_list(f):
    l = []
    n = 1
    while len(str(f(n))) <= 4:
        if len(str(f(n))) < 4:
            n += 1
            continue
        l.append(str(f(n)))
        n += 1
    return l

from time import time

start_time = time()

d = {}  # dictionary of figurate numbers
d[3] = get_list(lambda n: n*(n+1)/2)
d[4] = get_list(lambda n: n**2)
d[5] = get_list(lambda n: n*(3*n-1)/2)
d[6] = get_list(lambda n: n*(2*n-1))
d[7] = get_list(lambda n: n*(5*n-3)/2)
d[8] = get_list(lambda n: n*(3*n-2))

# 4 digit numbers -> 3:96, 4:68, 5:56, 6:48, 7:43, 8:40
# 351 total numbers
# 299 unique numbers
count = 0
numbers = set()
for i in range(3, 9):
    count += len(d[i])
    numbers = numbers.union(set(d[i]))
    print "%d: %d %s" % (i, len(d[i]), d[i])
# print count
# print len(numbers)
# print len(d[3]+d[4]+d[5]+d[6]+d[7]+d[8])

c = {}  # list of cyclic numbers that can follow a number
last_two_digits = {}  # list of cyclic numbers that starts with a 2 digit number
for i in range(3, 9):
    for j in range(3, 9):
        for n1 in d[i]:
            for n2 in d[j]:
                if i != j and n1[-2:] == n2[:2]:
                    if (i, n1) in c:
                        c[(i, n1)].append((j, n2))
                    else:
                        c[(i, n1)] = [(j, n2)]

                    if n1[:2] in last_two_digits:
                        if not (i, n1) in last_two_digits[n1[:2]]:
                            last_two_digits[n1[:2]].append((i, n1))
                    else:
                        last_two_digits[n1[:2]] = [(i, n1)]

print c
print len(c)
print last_two_digits
print len(last_two_digits)

results = []
for n1 in c:
    for n2 in c[n1]:
        if not n2[1][-2:] in last_two_digits:
            continue
        used = [n1[0], n2[0]]
        for n3 in last_two_digits[n2[1][-2:]]:
            if n3[0] in used:
                continue
            used = [n1[0], n2[0], n3[0]]
            for n4 in c[n3]:
                if n4[0] in used:
                    continue
                if not n4[1][-2:] in last_two_digits:
                    continue
                used = [n1[0], n2[0], n3[0], n4[0]]
                for n5 in last_two_digits[n4[1][-2:]]:
                    if n5[0] in used:
                        continue
                    used = [n1[0], n2[0], n3[0], n4[0], n5[0]]
                    for n6 in c[n5]:
                        if n6[0] in used:
                            continue
                        if n6[1][-2:] == n1[1][:2]:
                            results.append([n1, n2, n3, n4, n5, n6])

print results

sum_ = 0
for n in results[0]:
    sum_ += int(n[1])

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Sat, 12 Apr 2014, 02:45
# Solve by: 12430
# ---------------
# [[(6, '8128'), (5, '2882'), (3, '8256'), (4, '5625'), (7, '2512'), (8, '1281')]]
# Answer: 28684
# Total Time:  0.197000026703
# [Finished in 0.4s]
