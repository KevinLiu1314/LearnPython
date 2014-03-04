# -*- coding: utf-8 -*-

def mykey(t):
    return t[1], t[0]

f = open("budda.txt")
text = f.read().decode('utf-8')
f.close()

d = {}
for c in text:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

d_as_list = sorted(d.items(), key=mykey, reverse=True)

# f = open("budda clean.txt", "w")
# for t in d_as_list:
#     f.write("%s,%d\n" % (t[0].encode('utf-8'), t[1]))

# f.close()



for c in sorted(d):
    print "%s %d" % (c.encode('utf-8'), d[c])

# # -*- coding: utf-8 -*-

# str = "東海大學 Tunghai University".decode('utf-8')

# f = open("test.txt",'w')
# f.write("%s" % str.encode('utf-8'))
# f.close()

# print str