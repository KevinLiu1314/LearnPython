# -*- coding: utf-8 -*-
# Problem 203
# Squarefree Binomial Coefficients

# The binomial coefficients nCk can be arranged in triangular form, Pascal's
# triangle, like this:
#     1
#     1       1
#     1       2       1
#     1       3       3       1
#     1       4       6       4       1
#     1       5       10      10      5       1
#     1       6       15      20      15      6       1
#     1       7       21      35      35      21      7       1
# .........

# It can be seen that the first eight rows of Pascal's triangle contain twelve
# distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

# A positive integer n is called squarefree if no square of a prime divides n.
# Of the twelve distinct numbers in the first eight rows of Pascal's triangle,
# all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers
# in the first eight rows is 105.

# Find the sum of the distinct squarefree numbers in the first 51 rows of
# Pascal's triangle.

from time import time
from UsefulFunctions import primes


def square_free(n):
    pgen = primes()
    p = next(pgen)
    while p ** 2 <= n:
        if n % p ** 2 == 0:
            return False
        p = next(pgen)

    return True


def next_row(row):
    new_row = [1]
    for i in range(1, len(row)):
        new_row.append(row[i - 1] + row[i])
    new_row.append(1)

    return new_row

start_time = time()

N = 51
row = [1]
numbers = [1]
for i in range(N - 1):
    row = next_row(row)
    numbers = numbers + row

unique_numbers = set(numbers)
square_free_numbers = []
for n in unique_numbers:
    if square_free(n):
        square_free_numbers.append(n)

print "Answer:", sum(square_free_numbers)

print "Total Time: ", time() - start_time

# Completed on Thu, 27 Mar 2014, 00:03
# Solve by: 5236
# ---------------
# Answer: 34029210557338
# Total Time:  71.8900001049
# [Finished in 72.1s]
