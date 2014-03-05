# Problem 5
# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?


def pf(n):
    l = []
    d = 2
    while n > 1:
        while n % d == 0:
            l.append(d)
            n /= d

        d += 1

    return l

# Method 1, takes few minutes
# l = [i for i in range(2, 21)]
# print l
# n = 1
# while True:
#     if all(n % x == 0 for x in l):
#         print n
#         break
#     n += 1

# Method 2
sm = []
for d in range(2, 21):
    pf_of_d = pf(d)
    print d, " -> ", sm, ':', pf_of_d
    sm_temp = sm[:]
    for i in range(len(pf_of_d)):
        if pf_of_d[i] in sm_temp:
            del sm_temp[sm_temp.index(pf_of_d[i])]

    sm = sm_temp + pf_of_d

print reduce(lambda x, y: x * y, sm)

# Completed on Sat, 1 Mar 2014, 21:53
# Solve by: 207961
# ---------------
# 232792560
# [Finished in 0.2s]
