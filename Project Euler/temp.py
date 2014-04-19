i = 1
gpn = 1     # generalized pentagonal numbers

while i < 20:
        print i, gpn
        i += 1
        if i % 2 == 1:
            j = i / 2 + 1
        else:
            j = - i / 2
        gpn = (3*j**2-j)/2
