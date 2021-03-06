# Problem 1
# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

l = range(1, 1000)
l = filter(lambda x: x % 3 == 0 or x % 5 == 0, l)
print "Sum is: ", sum(l)
l = reduce(lambda x, y: x + y, l)

print l

# Completed on Sat, 1 Mar 2014, 18:34
# Solve by: 353082
# ---------------
# Sum is:  233168
# 233168
# [Finished in 0.1s]
