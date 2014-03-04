# Problem 22
# Names scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.

# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 X 53 = 49714.

# What is the total of all the name scores in the file?

names = sorted(open("problem 22.txt").read().replace('"', "").split(","))
avalues = [sum(map(lambda x: ord(x) - ord("A") + 1, list(name))) for name in names]
scores = [(names.index(names[i]) + 1) * avalues[names.index(names[i])] for i in range(len(names))]
print names
print avalues
print names.index("COLIN")
print avalues[937]
print scores[937]

print sum(scores)

# Answer: 871198282
