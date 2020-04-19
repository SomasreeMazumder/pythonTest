from builtins import sum
class Coures:
    def __init__(self, name, ratings):
        self.name=name
        self.rating=ratings
       
    def average(self):
         #numberofratings=self.rating
        numberofratings = len(self.rating)
        average = sum(self.rating)/numberofratings
        print("Average rating: ",self.name,"Is", average)

c1=Coures("Java Course",[1,2,3,4])
print(c1.name)
print(c1.rating)

c2=Coures("Java Webservice",[1,2,3,4])
print(c2.name)
print(c2.rating)
c2.average()
