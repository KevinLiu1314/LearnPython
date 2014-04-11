# -*- coding: utf-8 -*-
# Problem 104
# Pandigital Fibonacci ends

# The Fibonacci sequence is defined by the recurrence relation:

#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# It turns out that F541, which contains 113 digits, is the first Fibonacci
# number for which the last nine digits are 1-9 pandigital (contain all the
# digits 1 to 9, but not necessarily in order). And F2749, which contains 575
# digits, is the first Fibonacci number for which the first nine digits are 1-9
# pandigital.

# Given that Fk is the first Fibonacci number for which the first nine digits
# AND the last nine digits are 1-9 pandigital, find k.

from time import time


def fibonacci():
    f1 = 1
    yield f1

    f2 = 1
    yield f2
    while True:
        yield f1 + f2
        f1, f2 = f2, f1 + f2

start_time = time()

fgen = fibonacci()  # fibonacci generator
k = 0
nine_digits = set("123456789")
while True:
    f = next(fgen)
    k += 1
    last_nine_digits = f % 1000000000   # convert to a string takes toooo long
    if nine_digits == set(str(last_nine_digits)):
        f_str = str(f)
        first_nine_digits = f_str[:9]
        if nine_digits == set(first_nine_digits):
            print "length: ", len(f_str)
            break

print "Answer:", k

print "Total Time: ", time() - start_time

# Completed on Wed, 2 Apr 2014, 00:00
# Solve by: 8706
# ---------------
# length:  68855
# Answer: 329468
# Total Time:  123.910000086
# [Finished in 124.1s]
