class Programmer:
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name

    def setSalary(self,s):
        self.salary=s
    def getSalary(self):
        return self.salary

    def setTechnologies(self,t):
        self.technology=t
    def getTechnologies(self):
        return self.technology

p1=Programmer()
p1.setSalary("10000")
p1.setName("Nilay")
p1.setTechnologies("Advance Java")

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())