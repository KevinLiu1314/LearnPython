f = open("test.txt")
text = f.read().decode('utf-8')
f.close()

print text

for c in text:
    print c,

print "\n------------"

for i in range(len(text)):
    print text[i],
