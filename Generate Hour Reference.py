import datetime

a = 0
f = open('Hour Reference.txt', 'w')
while True:
    t = datetime.datetime(2012, 10, 1, 0, 0, 0) + datetime.timedelta(hours=a)
    if t == datetime.datetime(2016, 1, 1): break
    f.write(t.strftime('%m/%d/%Y %H:%M:%S')+'\n')
    a = a + 1

f.close()
