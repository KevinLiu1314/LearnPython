# Problem 20
# Factorial digit sum

# n! means n X (n - 1) X ... X 3 X 2 X 1

# For example, 10! = 10 X 9 X ... X 3 X 2 X 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math

f = math.factorial(100)
f_digits = map(lambda x: int(x), list(str(f)))
print sum(f_digits)

# Completed on Mon, 3 Mar 2014, 01:49
# Solve by: 98269
# ---------------
# 648
# [Finished in 0.2s]
