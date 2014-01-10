def mymain():
    add_many(5,6,3,2)
    add_many(2)
    add_many()


def add_many(*args):
    total=0
    for arg in args:
        total +=arg
    print args, "=", total


class Pet(object):
    def __init__(self, name, species, breed):
        self.name=name
        self.species=species
        self.breed=breed

    def print_animal(self):
        print self.name
        print self.species
        print self.breed

fish=Pet(name='Coe', species='fish', breed="betta")
fish.print_animal()

        
class Student(object):
    def __init__(self, last, first, dob, grades=[], extra=0):
        self.last=last
        self.first=first
        self.dob=dob
        self.grades=grades
        self.extra=extra

    def print_grades(self):
        for grade in self.grades:
            print "Test:", grade

    def get_average(self):
        total=0
        for grade in self.grades:
            total += grade
        return (total+self.extra)/len(self.grades)

    def print_student(self):
        print self.first, self.last
        print "DOB:", self.dob

    def print_report(self):
        self.print_student()
        self.print_grades()
        print "Extra credit:", self.extra
        print "Average:", self.get_average()

def newmain():
    s=Student(last="Wei",
              first="June",
              grades=[87,94,89],
              extra=20,
              dob='06/21/92')
    s.print_report()
    

        
if __name__ == "__main__":
    mymain()
    newmain()

        
