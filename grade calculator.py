print "this is the grade calculator".title()

last=raw_input("Last name: ")
first=raw_input("First name: ")

tests=[]

while True:
    test=input("Grade: ")
    if test<0 : break
    tests.append(test)

total=0

for test in tests:
    total=total+test
    
print "*" * 20

i=1
for test in tests:
    print "Test #{i}: {grade}".format(i=i,grade=test)
    i=i+1

print "*"*20
print "Average:", total/len(tests)



def hello3(name=8):
    print "hello"
    print "you name is",name

hello3("ml")
