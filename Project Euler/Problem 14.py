# Problem 14
# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def cs(n):
    l = 1   # adjust for initial value
    next_num = f(n)
    while next_num != 1:
        l += 1
        next_num = f(next_num)
    l += 1  # adjust for last 1

    return l

# Method 1 - took 43 seconds,
n = 1
max_cs = 0
for i in range(1, 1000000):
    cs_for_i = cs(i)
    if cs_for_i > max_cs:
        n = i
        max_cs = cs_for_i

# Method 2 - took 45 seconds
# n = 1
# max_cs = 0
# i = 1
# while i < 1000000:
#     cs_for_i = 1    # adjust for initial value
#     if i % 2 == 0:
#         next_num = i / 2
#     else:
#         next_num = 3 * i + 1

#     while next_num != 1:
#         if next_num % 2 == 0:
#             next_num = next_num / 2
#         else:
#             next_num = 3 * next_num + 1

#         cs_for_i += 1

#     cs_for_i += 1   # adjust for last 1

#     if cs_for_i > max_cs:
#         n = i
#         max_cs = cs_for_i

#     i += 1

print n, max_cs

# Completed on Sun, 2 Mar 2014, 04:51
# Solve by: 102378
# ---------------
# 837799 525
# [Finished in 49.0s]
