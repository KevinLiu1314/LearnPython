# Problem 3
# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?


def lpf(n):
    if n < 2:
        return n

    d = 2
    while n > 1:
        divisor_so_far = d
        while n % d == 0:
            n /= d

        d += 1

    return divisor_so_far

print lpf(600851475143)

# Completed on Sat, 1 Mar 2014, 19:47
# Solve by: 213234
# ---------------
# 6857
# [Finished in 0.2s]
