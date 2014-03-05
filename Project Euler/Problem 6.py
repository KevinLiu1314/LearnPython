# Problem 6
# Sum square difference

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

sum_of_square = sum(i ** 2 for i in range(1, 101))
square_of_sum = sum(i for i in range(1, 101)) ** 2

print square_of_sum - sum_of_square

# Completed on Sat, 1 Mar 2014, 22:36
# Solve by: 209539
# ---------------
# 25164150
# [Finished in 0.2s]
