class Person:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("I am inside parent by default")

    def getName(self):
        print("my name is:" + self.x)

    def getAge(self):
        print("My age:r" + self.y)


class Child(Person):
    # def __init__(self): #commenitng this __init__ to stop initialization and take the properties of Parent into child class
    #     print("I am inside child by default")

    def getChild(self):
        print("I am Only Child")

    def getPprop(self):
        p.getName()
        p.getAge()

    def newm(self):  # Child's method
        Person.getName(self)  # parent method #Person is having two values. So instead of varible p, person class is called/used of method overriding
        Person.getAge(self)  #for method overriding Person is called/used
    # p.getAge(self)      #parent method
    def newF(self):
        return self.x

p = Person("sanchari", "27")
#p1 = Person("abc",23)

p.getName()
p.getAge()

c = Child("abc", "1234")# overriding happening here
c.getChild()
c.getPprop()
c.newm()
#c.newm("abc", "1234")
#c.newm('abc')

