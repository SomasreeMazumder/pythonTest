class Student:
    major='CSE'
    def __init__(self,rollname,name):
        self.rollname=rollname
        self.name=name
s1=Student(1,'Jhon')
s2=Student(2,'Bill')
print(s1.major)
print(s1.name)
print(s1.rollname)
print(s2.major)
print(s2.name)
print(s2.rollname)