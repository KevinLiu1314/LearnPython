# -*- coding: utf-8 -*-
# Problem 42
# Coded triangle numbers

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
# so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
# is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are
# triangle words?

from time import time

start_time = time()

# this should be more than enough, T29=435, (Z)26 X 20 = 520
tn_list = [n*(n+1)/2 for n in range(1, 30)]
print tn_list

words = open("problem 42.txt").read().replace('"', "").split(',')
print words

values = [[ord(w[i])-ord('A')+1 for i in range(len(w))] for w in words]
print values
print "maximum: %d" % max([sum(v) for v in values])

coded = filter(lambda n: n in tn_list, [sum(v) for v in values])
print coded
print len(coded)

print "Total Time: ", time() - start_time

# Completed on Wed, 5 Mar 2014, 00:37
# Solve by: 38102
# ---------------
# 162
# Total Time:  0.388999938965
# [Finished in 0.6s]
