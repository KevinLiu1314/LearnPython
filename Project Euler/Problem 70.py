# -*- coding: utf-8 -*-
# Problem 70
# Totient permutation

# Euler's Totient function, φ(n) [sometimes called the phi function], is used to
# determine the number of positive numbers less than or equal to n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
# nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number,
# so φ(1)=1.

# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
# of 79180.

# Find the value of n, 1<n<10^7, for which φ(n) is a permutation of n and the
# ratio n/φ(n) produces a minimum.

# 1. http://en.wikipedia.org/wiki/Euler%27s_totient_function#Generating_functions
# 2. square root of 10000000 is 3162
# 3. we are looking for two primes to minimize n/φ(n)
# 4. n = product of two primes 2000 < p1, p2 < 4000
# 5. phi = φ(n) = n(1-1/p1)(1-1/p2) = n(1-1/p1)(1-1/p2) * p1/p1 * p2/p2
# 6. phi = n/(p1*p2)*p1(1-1/p1)*p2(1-1/p2)
# 7. phi = (p1-1)(p2-1)


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

from time import time

start_time = time()

pgen = sieve(4000)
primes = []
p = next(pgen)
while p < 2000:
    p = next(pgen)
while p < 4000:
    primes.append(p)
    try:
        p = next(pgen)
    except StopIteration:
        break

candidates = []
for i in xrange(len(primes)-1):
    for j in xrange(i+1, len(primes)):
        n = primes[i] * primes[j]
        if n > 10000000:
            break
        phi = (primes[i]-1) * (primes[j]-1)
        if is_permutation(n, phi):
            candidates.append((float(n)/phi, n, phi))

print min(candidates)

print "Answer:", min(candidates)[1]

print "Total Time: ", time() - start_time

# Completed on Thu, 24 Apr 2014, 03:38
# Solve by: 11473
# ---------------
# (1.0007090511248113, 8319823, 8313928)
# Answer: 8319823
# Total Time:  0.101999998093
# [Finished in 0.3s]
