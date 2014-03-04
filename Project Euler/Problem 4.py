# Problem 4
# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 X 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

p = []
for n1 in range(100, 1000):
    for n2 in range(100, 1000):
        product_str = str(n1 * n2)
        if product_str == product_str[::-1]:
            p.append(n1 * n2)

print max(p)
