# Problem 26
# Reciprocal cycles

# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit raw_fractions with denominators 2 to 10 are given:

#     1/2 =   0.5
#     1/3 =   0.(3)
#     1/4 =   0.25
#     1/5 =   0.2
#     1/6 =   0.1(6)
#     1/7 =   0.(142857)
#     1/8 =   0.125
#     1/9 =   0.(1)
#     1/10    =   0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.
import decimal
decimal.getcontext().prec = 2000
from time import time

def repeats(first_str, second_str):
    """
    returns true if the first string repeats in the second string
    we assume if the first_str repeats consecutively for 2 times,
    then it's considered as repeating
    """
    first_occurance = second_str.find(first_str)
    second_occurance = second_str.find(first_str, first_occurance + len(first_str))
    if first_occurance + len(first_str) == second_occurance:
        return True
    else:
        return False

start_time = time()

# 1. calculate each fraction to 100 decimal places
# 2. store only the decimal places in the fractions list, all 999 of them
# 3. loop through these 999 decimals and see if any length(0 < n < 30) is repeating
# 4. if any testing string is repeating, add the index & repeating length to a list of (repeat_len, i)
# 5. look for the max length and it's corresponding d, where d = index + 1
raw_fractions = [str(decimal.Decimal(1) / decimal.Decimal(d)) for d in range(1, 1000)]
fractions = map(lambda x: x.rstrip("0")[2:], raw_fractions)

i = 0
repeating_numbers = []
while i < 999:
    for repeat_len in range(2, 1000):     # going to try substring of various lengths
        start = 0
        is_repeating = repeats(fractions[i][start:start + repeat_len], fractions[i])
        while not is_repeating:
            start += 1
            if start + repeat_len > 2000:     # not repeating for all substrings with this repeat_len
                break
            is_repeating = repeats(fractions[i][start:start + repeat_len], fractions[i])

        if is_repeating:    # some digits are repeating, save this fraction & it's repeat_len
            repeating_numbers.append((repeat_len, i + 1))
            break

    i += 1

print "len: %d   d: %d" % max(repeating_numbers)

print "Total Time: ", time() - start_time

