from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        # print("Starting the car")
        pass

    @abstractmethod
    def stop(self):
        pass
    # print("stopping the car")

    @abstractmethod  # 1. declare the method with @abstract key word
    def drive(self):
        pass  # abstraction


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        # BMW.__init__(self,make,model,year)# this ReUsability. We can reuse the qualities of parent. It is inheretence
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print("*****" + str(self.cruiseControlEnabled))
        super().start()

    def start(self):
        super().start();
        print("Button Start")

    def stop(self):
        super().stop()
        print("I am in ThreeSeries stop")
    def drive(self):
        print("Three series is being driven")
        # BMW.drive()



class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        # BMW.__init__(self, make, model, year)# this is ReUsability. We can reuse the qualities of parent. it is inheretence
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def drive(self):
        print("Five FiveSeries is being driven")

    def start(self):
        super().start();
        print("Remote Start")

    def stop(self):
        super().stop()
        print("I am in FiveSeries stop")


threeSeries = ThreeSeries(True, "BMW", '328i', "2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()  # functionality can be inhereted which is also reusability
threeSeries.stop()
print(threeSeries.display())
print("**********************************************")
fiveSeries = FiveSeries(False, "Audi", '328i', "2018")
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.stop()#initially there stop and start method were from parent class in inhetence. now it is under interface means
fiveSeries.start()#all are abstract method and needs to be implemented 

# b=BMW("Audi", '328i', "2018")
