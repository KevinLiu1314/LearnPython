# -*- coding: utf-8 -*-
# Problem 131
# Prime cube partnership

# There are some prime values, p, for which there exists a positive integer, n,
# such that the expression n3 + n2p is a perfect cube.

# For example, when p = 19, 83 + 82×19 = 123.

# What is perhaps most surprising is that for each prime with this property the
# value of n is unique, and there are only four such primes below one-hundred.

# How many primes below one million have this remarkable property?

# 1. n^3 + n^2*p = k^3
# 2. n^3(1+p/n) = k^3
# 3. n^3((n+p/n) = k^3
# 4. n * cuberoot((n+p)/n) = k
# 5. for k to be integer, n+p & n must also be perfect cube
# 6. let n=x^3 and n+p=y^3
# 7. p=y^3-x^3, so p is the difference of two cubes
# 8. p=y^3-x^3=(y-x)(y^2+xy+x^2), in order for p to be prime, y-x must be 1
# 9. so we are checking if the difference of two cubes is a prime number

from time import time


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

start_time = time()

N = 1000000
count = 0
i = 1
while True:
    p = (i + 1) ** 3 - i ** 3
    if p >= N:
        break
    if is_prime(p):
        count += 1
    i += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Thu, 1 May 2014, 01:52
# Solve by: 3997
# ---------------
# Answer: 173
# Total Time:  0.0210001468658
# [Finished in 0.2s]
