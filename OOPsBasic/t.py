'''class Student:
    major = "Math"

    def __init__(self, rollnumber, stu):
        self.rollnumber = rollnumber
        self.x = stu


s1 = Student(1, "som")
s2 = Student(2, "somss")
print(s1.major)
print(s2.major)
print(s1.x)
print(s2.x)'''

'''''class course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings


c1 = course("Riys", [123, 455])
print(c1.name)
print(c1.ratings)

c2 = course("Rimi", [1457, 455])
print(c1.name)
print(c1.ratings)'''

'''class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        # BMW __init__ (self,make,model,year)
        super() __init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled


def __init__(make, model, year):
    pass


class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        # BMW__init__(self,make,model,year)
        super() __init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


threeSeries = ThreeSeries(True,"BMW", "98rm", "1998")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
'''


class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):

        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Starrting Airbus Engine")


class BoingEngine:
    def start(self):
        print("Starting Boing Engine")


ae = AirbusEngine()
f = Flight(ae)
f.startEngine()

be = BoingEngine()
f1 = Flight(be)
f1.startEngine()
