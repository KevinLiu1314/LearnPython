# Problem 2
# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms.  By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.


def f(upperbound):
    a = 1
    yield a
    b = 1
    yield b
    while a + b < upperbound:
        yield a + b
        a, b = b, a + b

# Method 1
s = 0
for i in f(4000000):
    if i % 2 == 0:
        s += i

print s

# Method 2
l = [i for i in f(4000000)]
l = filter(lambda x: x % 2 == 0, l)
print sum(l)

# Completed on Sat, 1 Mar 2014, 19:29
# Solve by: 291879
# ---------------
# 4613732
# 4613732
# [Finished in 0.2s]
