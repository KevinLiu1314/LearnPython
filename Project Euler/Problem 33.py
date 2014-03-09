# -*- coding: utf-8 -*-
# Problem 33
# Digit canceling fractions

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.


from time import time

start_time = time()

# Method 1, could simplified a little as in Method 2
# l = []
# for numerator in range(10, 100):
#     for denominator in range(numerator + 1, 100):   # insure the fraction is less than 1
#         if numerator % 10 == 0 and denominator % 10 == 0:   # Trivial cases 10/20, 30/40, etc.
#             continue

#         common_digit = list(set(str(numerator)) & set(str(denominator)))
#         if len(common_digit) != 1:   # either too many common digits or too few
#             continue

#         # ", 1" is needed in cases like 11, or else it will reduct to "",
#         # which will get an error when converting to int
#         new_numerator = int(str(numerator).replace(common_digit[0], "", 1))
#         new_denominator = int(str(denominator).replace(common_digit[0], "", 1))
#         if new_denominator == 0:    # don't want to divide by 0
#             continue
#         if float(numerator)/float(denominator) == float(new_numerator)/float(new_denominator):
#             l.append((new_numerator, new_denominator))

# print l
# print reduce(lambda f1, f2: (f1[0]*f2[0], f1[1]*f2[1]), l)

# print "Total Time: ", time() - start_time

# Completed on Sat, 8 Mar 2014, 02:13
# Solve by: 35085
# ---------------
# [(1, 4), (1, 5), (2, 5), (4, 8)]
# (8, 800)
# Total Time:  0.0230000019073
# [Finished in 0.2s]

# Method 2, if the numerator or the denominator is divisible by 10, just skip it
l = []
for numerator in range(11, 100):
    for denominator in range(numerator + 1, 100):   # insure the fraction is less than 1
        if numerator % 10 == 0 or denominator % 10 == 0:   # Trivial cases 10/20, 30/40, etc. & 12/20, 10/33, etc.
            continue

        common_digit = list(set(str(numerator)) & set(str(denominator)))
        if len(common_digit) != 1:  # either too many common digits or too few
            continue

        # ", 1" is needed in cases like 11, or else it will reduct to "",
        # which will get an error when converting to int
        new_numerator = int(str(numerator).replace(common_digit[0], "", 1))
        new_denominator = int(str(denominator).replace(common_digit[0], "", 1))
        if float(numerator)/float(denominator) == float(new_numerator)/float(new_denominator):
            # l.append((new_numerator, new_denominator))
            l.append((numerator, denominator))

print l
print reduce(lambda f1, f2: (f1[0]*f2[0], f1[1]*f2[1]), l)

print "Total Time: ", time() - start_time
