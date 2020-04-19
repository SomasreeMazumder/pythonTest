class Parent:
    def __init__(self):
        print("I am in parent.")

    def printParent(self):
        print("this  is parent")


class Child(Parent):
    def __init__(self):
        print("I am in child.")

    def printChild(self):
        print("this  is child")
    def Abc(self):
         Parent.printParent(self)
p=Parent()
p.printParent()

c = Child()
c.printChild()
c.printParent()#actual inheretence
c.Abc()





