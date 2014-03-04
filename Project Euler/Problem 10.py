# Problem 10
# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math


def primes():
    n = 2
    yield n

    n = 3
    yield n

    primes_so_far = [2, 3]      # takes care of index out of range case
                                # when n = 3 if initial is only [2]

    while True:
        n += 1
        divisor_index = 0
        is_prime = False
        while n % primes_so_far[divisor_index] != 0:
            divisor_index += 1
            if primes_so_far[divisor_index] > math.sqrt(n):
                is_prime = True
                break

        if is_prime:
            yield n
            primes_so_far.append(n)

p = primes()

sum = 0
next_p = next(p)
while next_p < 2000000:
    sum += next_p
    next_p = next(p)

print sum
