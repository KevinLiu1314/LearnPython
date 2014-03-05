# -*- coding: utf-8 -*-

def fibonacci():
    f1 = 1
    yield f1

    f2 = 1
    yield f2
    while True:
        yield f1 + f2
        f1, f2 = f2, f1 + f2


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


def triangle_numbers():
    """Formula Tn = ½n(n+1)"""
    n = 0
    i = 1
    while True:
        n += i
        yield n
        i += 1


def proper_factors(n):
    factors = [1]

    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            factors.append(d)
            if d != n / d:
                factors.append(n / d)
        d += 1

    return factors


def rotations(n):
    for i in range(len(str(n)) - 1):
        n = int(str(n)[1:] + str(n)[0])
        yield n


def palindromic(s):
    return all([s[i] == s[-(i + 1)] for i in range(len(s) / 2)])


def is_pandigital(n):
    return set(str(i) for i in range(1, len(str(n)) + 1)) == set(str(n))


# Triangle number generator
# Tn=n(n+1)/2         1, 3, 6, 10, 15, ...
def triangle_num_gen():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1


# Pentagonal number generator
# Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
def pentagonal_num_gen():
    n = 1
    while True:
        yield n * (3 * n - 1) / 2
        n += 1


# Hexagonal number generator
# Hn=n(2n−1)      1, 6, 15, 28, 45, ...
def hexagonal_num_gen():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1


# Usage Examples

# myf = triangle_numbers()
# for i in range(20):
#     print next(myf)

# for i in range(1, 100):
#     print i, " -> ", sorted(proper_factors(i))

# for i in range(1, 50):
#     print i, is_prime(i)

# for e in rotations(1978):
#     print e

# print palindromic("585")
# print palindromic("1001001001")

# print is_pandigital(7361425)
