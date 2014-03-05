# Problem 21
# Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).

# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


def d(n):
    sum = 0
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            sum += i

    return sum

anlist = []
for a in range(1, 10000):
    b = d(a)
    if a != b and a == d(b):
        # print "a=%d b=%d" % (a, b)
        if not a in anlist:
            anlist.append(a)
        if not b in anlist:
            anlist.append(b)

print sum(anlist)

# Completed on Mon, 3 Mar 2014, 02:11
# Solve by: 68676
# ---------------
# 31626
# [Finished in 4.0s]
