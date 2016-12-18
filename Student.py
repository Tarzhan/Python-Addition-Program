class Student:
    
    def __init__(self, name, lastname, studentnumber, course):
        self.name=name
        self.lastname=lastname
        self.studentnumber=studentnumber
        self.course=course

    def showDetails(self):
        print(self.name, self.lastname, self.studentnumber, self.course)


class main:
    person = Student("Jack", "Doe", "2132", "ISD")
