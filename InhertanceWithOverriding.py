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
     # def __init__(self):
     #     print("I am inside child by default")

     def getChild(self):
        print("I am Only Child")

     def getPprop(self):
        p.getName()
        p.getAge()

     def newm(self):  # Child's method
        Person.getName(self)  # parent method
        Person.getAge(self)
        #Person.getName(self) #not allowed as Person is having 2parameters where Child is not having any
        #p.getName(self) #not allowed as x varibale is not permitted as it is not defined into child class
    # p.getAge(self)      #parent method
    #def newF(self):
        #return self.x

p = Person("sanchari", "27")
#p1 = Person("abc",23)

p.getName()
p.getAge()

#c=Child()
c = Child("abc", "1234")
c.getChild()
c.getPprop()
c.newm()
#c.newm("abc", "1234")
#c.newm('abc')

