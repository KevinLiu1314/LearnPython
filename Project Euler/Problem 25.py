# Problem 25
# 1000-digit Fibonacci number

# The Fibonacci sequence is defined by the recurrence relation:

#     Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:

#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the first term in the Fibonacci sequence to contain 1000 digits?


def f():
    a = 1
    yield a
    b = 1
    yield b
    while True:
        yield a + b
        a, b = b, a + b

# Method 1
myf = f()

term = 0
while True:
    term += 1
    n = next(myf)
    if len(str(n)) >= 1000:
        print term
        break

# Completed on Tue, 4 Mar 2014, 00:53
# Solve by: 75083
# ---------------
# 4782
# [Finished in 0.4s]
