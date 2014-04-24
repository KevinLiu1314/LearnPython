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


def sieve(N):
    """
    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the first prime number.
    3. Starting from p, enumerate its multiples by counting to n in increments
       of p, and mark them in the list (these will be 2p, 3p, 4p, etc.; the p
       itself should not be marked).
    4. Find the first number greater than p in the list that is not marked.
       If there was no such number, stop. Otherwise, let p now equal this new
       number (which is the next prime), and repeat from step 3.
    """
    numbers = [1 for i in xrange(N + 1)]
    p = 2
    while p <= N:
        if numbers[p] == 1:     # a new prime number
            yield p
            for j in range(p, N + 1, p):
                numbers[j] = 0  # a multiple of p, not a prime
            numbers[p] = 1      # save our prime
        p += 1


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


def is_palindromic(s):
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


def hexagonal_num_gen():
    """
    Hexagonal number generator
    # Hn=n(2n−1)      1, 6, 15, 28, 45, ...
    """
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1


def is_terminal(n, d):
    """
    return True if n/d is terminal, False Otherwise
    """
    seen_before =[]
    remainder = n % d
    while not remainder in seen_before:
        if remainder == 0:
            return True
        seen_before.append(remainder)
        remainder = remainder * 10 % d

    return False


def baseconvert(n, base):
    """
    convert positive decimal integer n to equivalent in another base (2-36)
    """
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    if n < 0 or base < 2 or base > 36:
        return ""

    s = ""
    while True:
        r = n % base
        s = digits[r] + s
        n = n / base
        if n == 0:
            break

    return s

from fractions import Fraction as F
def convergent(terms):
    """
    return the convergent of the continue fraction expansion
    """
    i = len(terms) - 1           # expand from last term
    if i == 0:
        return F(terms[0], 1)

    f = F(1, terms[i])
    while i != 1:
        i -= 1
        f = F(terms[i], 1) + f
        f = F(f.denominator, f.numerator)

    return F(terms[0], 1) + f


def is_permutation(m, n):
    """
    check to see if m & n are permutations of each other
    checking to see if the frequency of the digits 0-9 are the same
    """
    l = [0] * 10
    while m > 0:
        l[m % 10] += 1
        m /= 10
    while n > 0:
        l[n % 10] -= 1
        n /= 10
    for i in l:
        if i != 0:
            return False
    return True

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

# print is_pandigital(221)

# print sieve(97)

# print is_terminal(10, 16)

# print baseconvert(8992, 7)

# print is_permutation(9997619, 9991796)
