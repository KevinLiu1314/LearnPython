# Problem 9
# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def find_abc():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            for c in range(b + 1, 1000):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    return a, b, c

a, b, c = find_abc()

print "a=%d, b=%d, c=%d" % (a, b, c)
print a * b * c
