class student:
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
s=student()
s.setId("1")

s.setName("Nilay")
print(s.getId())
print(s.getName())

