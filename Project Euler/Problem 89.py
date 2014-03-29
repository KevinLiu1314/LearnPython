# -*- coding: utf-8 -*-
# Problem 89
# Roman numerals

# The rules for writing Roman numerals allow for many ways of writing each number
# (see About Roman Numerals...). However, there is always a "best" way of writing
# a particular number.

# For example, the following represent all of the legitimate ways of writing the
# number sixteen:

# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI

# The last example being considered the most efficient, as it uses the least
# number of numerals.

# The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
# contains one thousand numbers written in valid, but not necessarily minimal,
# Roman numerals; that is, they are arranged in descending units and obey the
# subtractive pair rule (see About Roman Numerals... for the definitive rules
# for this problem).

# Find the number of characters saved by writing each of these in their minimal
# form.

# Note: You can assume that all the Roman numerals in the file contain no more
# than four consecutive identical units.

from time import time


def int_to_roman(n):
    parts = []
    for roman, value in Table:
        while value <= n:
            n -= value
            parts.append(roman)

    return ''.join(parts)


def roman_to_int(r):
    result = 0
    for roman, value in Table:
        while r.startswith(roman):
            result += value
            r = r[len(roman):]

    return result

start_time = time()

Table = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
         ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

original = open("Problem 89.txt").read().splitlines()
numbers = map(roman_to_int, original)
new_romans = map(int_to_roman, numbers)
original_len = map(len, original)
new_romans_len = map(len, new_romans)

print "Answer:", sum(original_len) - sum(new_romans_len)

print "Total Time: ", time() - start_time

# Completed on Sat, 29 Mar 2014, 03:26
# Solve by: 11286
# ---------------
# Answer: 743
# Total Time:  0.0139999389648
# [Finished in 0.2s]
