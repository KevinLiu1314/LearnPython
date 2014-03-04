# Problem 12
# Highly divisible triangular number

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

import math


def tn():
    n = 0L
    i = 1L
    while True:
        n += i
        yield n
        i += 1


def factors(n):
    f = 0
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            f += 1

    return f + 1

# Method 1      This took more than 45 minutes & over 200MB without an answer
# mytn = tn()
# while True:
#     n = next(mytn)
#     if factors(n) >= 500:
#         print n
#         break

# Method 2 - takes only 23 seconds
n = 0
i = 1
while True:
    n += i

    # how many factors
    f = 0
    d = 1
    while d < math.sqrt(n):
        if n % d == 0:
            f += 1
        d += 1

    f *= 2
    if d == math.sqrt(n):   # in cases like 36 [1, 2, 3, 4, 6, 9, 12, 18, 36]
        f += 1

    if f >= 500:
        print n
        break

    i += 1

# Answer: 76576500
