# -*- coding: utf-8 -*-
# Problem 51
# Prime digit replacements

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated
# numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
# 56993. Consequently 56003, being the first member of this family, is the
# smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

# 1. check only 3 repeating digits
# 2. repeat digits can only be 0, 1, and 2, or else we won't get an eight family
# 3. assuming this smallest prime is a 5 digit one


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
            if primes_so_far[divisor_index] ** 2 > n:
                is_prime = True
                break

        if is_prime:
            yield n
            primes_so_far.append(n)


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        
        d += 1

    return True


def family_of_eight(p, replacement):
    """
    replace replacement in p with 0-9 and check if we have a eight member family
    """
    count = 0
    for digit in "0123456789":
        n = int(p.replace(replacement, digit))
        if n > 100000 and is_prime(n):
            count += 1

    return count == 8

from time import time

start_time = time()

pgen = primes()     # prime generator
while True:
    p = next(pgen)
    if p < 100000:  # guessing, we are looking for a five digit prime
        continue
    p_str = str(p)
    if p_str.count("0") == 3 and family_of_eight(p_str, "0") or \
        p_str.count("1") == 3 and family_of_eight(p_str, "1") or \
        p_str.count("2") == 3 and family_of_eight(p_str, "2"):
        break

print "Answer:", p

print "Total Time: ", time() - start_time

# Completed on Wed, 9 Apr 2014, 23:17
# Solve by: 15595
# ---------------
# Answer: 121313
# Total Time:  0.344000101089
# [Finished in 0.6s]
