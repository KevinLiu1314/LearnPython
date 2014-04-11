# -*- coding: utf-8 -*-
# Problem 60
# Prime pair sets

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
# primes, 792, represents the lowest sum for a set of four primes with this
# property.

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.


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


def ok(*prime_list):
    """
    determine if the "prime_list" is in the candidate set so far
    """
    if len(prime_list) == 1:
        return prime_list[0] in concatenatables

    for i in xrange(len(prime_list) - 1):
        if not prime_list[i] in concatenatables:
            return False
        list_to_check = concatenatables[prime_list[i]]
        for j in xrange(i + 1, len(prime_list)):
            if not prime_list[j] in list_to_check:
                return False

    return True

from time import time

start_time = time()

primes = [p for p in sieve(30000)]
concatenatables = {}
for a in xrange(len(primes) - 1):
    for b in xrange(a + 1, len(primes)):
        if is_prime(int(str(primes[a]) + str(primes[b]))) and is_prime(int(str(primes[b]) + str(primes[a]))):
            if primes[a] in concatenatables:
                concatenatables[primes[a]].append(primes[b])
            else:
                concatenatables[primes[a]] = [primes[b]]

print "Built dictionary: ", time() - start_time
print "Len: ", len(concatenatables)

results = []
for a in xrange(len(primes) - 4):
    if not ok(primes[a]):
        continue
    for b in xrange(a + 1, len(primes) - 3):
        if not ok(primes[a], primes[b]):
            continue
        for c in xrange(b + 1, len(primes) - 2):
            if not ok(primes[a], primes[b], primes[c]):
                continue
            for d in xrange(c + 1, len(primes) - 1):
                if not ok(primes[a], primes[b], primes[c], primes[d]):
                    continue
                for e in xrange(d + 1, len(primes)):
                    if ok(primes[a], primes[b], primes[c], primes[d], primes[e]):
                        results.append([primes[a], primes[b], primes[c], primes[d], primes[e]])

print results

print "Answer:", min(map(sum, results))

print "Total Time: ", time() - start_time

# Completed on Fri, 11 Apr 2014, 00:20
# Solve by: 12383
# ---------------
# Built dictionary:  3465.41599989
# Len:  3169
# [[7, 1237, 2341, 12409, 18433], [13, 5197, 5701, 6733, 8389], [467, 941, 2099, 19793, 25253]]
# Answer: 26033
# Total Time:  4030.62299991
# [Finished in 4030.8s]
