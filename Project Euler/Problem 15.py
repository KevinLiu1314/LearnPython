# Problem 15
# Lattice paths

# Starting in the top left corner of a 2X2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20X20 grid?

# Method 1, memory for 20 X 20 grid
# def routes(a, b, rows, columns):
#     if a == rows and b == columns:
#         return [[(a, b)]]

#     down = []
#     right = []

#     # all routes at next down coordinate
#     if a < rows:
#         down = routes(a + 1, b, rows, columns)

#     for i in range(len(down)):
#         down[i].append((a, b))

#     # all routes at next right coordinate
#     if b < columns:
#         right = routes(a, b + 1, rows, columns)

#     for i in range(len(right)):
#         right[i].append((a, b))

#     return down + right

# for r in routes(0, 0, 2, 2):
#     print r

# print len(routes(0, 0, 20, 20))


# Method 2 - running without result
# def routes(a, b, rows, columns):
#     if a == rows or b == columns:
#         return 1

#     # all routes at next down coordinate
#     down = 0
#     if a < rows:
#         down = routes(a + 1, b, rows, columns)

#     # all routes at next right coordinate
#     right = 0
#     if b < columns:
#         right = routes(a, b + 1, rows, columns)

#     return down + right

# print routes(0, 0, 2, 3)

# Method 3
rows = 20
columns = 20

# x = [[foo for i in range(10)] for j in range(10)]
# [x[:] for x in [[foo]*10]*10]
grid = [[1] + [0] * columns for j in range(rows + 1)]
for i in range(columns):
    grid[0][i + 1] = 1

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

print grid[rows]

# Answer: 137846528820L
