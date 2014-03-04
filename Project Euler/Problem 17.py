# Problem 17
# Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
         7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
         12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
         16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
         20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety', 1000: 'one thousand'}


def to_words(n):
    if n in words:
        return words[n]

    beginning = ""
    hundreds = n / 100
    if hundreds > 0:
        beginning = words[hundreds] + " hundred"

    n = n - hundreds * 100
    tens = n / 10 * 10
    units = n % 10
    ending = ""

    if n in words:
        ending = words[n]
    else:
        if tens > 0:
            ending = words[tens]
        if units > 0:
            if ending != "":
                ending = ending + " " + words[units]
            else:
                ending = words[units]

    if beginning != "":
        if ending != "":
            return beginning + " and " + ending
        else:
            return beginning
    else:
        return ending

# for i in range(800, 901):
#     print to_words(i)

oneline = ""
for i in range(1, 1001):
    oneline += to_words(i)

print len(oneline.replace(" ", ""))

# Answer: 21124
