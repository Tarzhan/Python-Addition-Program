from Student import * 

#p0 = Student()
p1 = Student("Girish", "Badass", "1234", "ISD")
p2 = Student("Saul", "Husdon", "1233", "WD")
p3 = Student("Bell", "Beast", "1232", "ISD")

Student = [p1, p3]
for p in Student:
    print()
    p.showDetails()
