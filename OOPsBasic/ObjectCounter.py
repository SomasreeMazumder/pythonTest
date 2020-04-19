class ObjectCounter:
    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    @staticmethod  # static method
    def displayCount():
        print(ObjectCounter.numberOfObjects)


o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.displayCount()

print(o1.displayCount())
print(o1.numberOfObjects)
print(o2.displayCount())
print(o2.numberOfObjects)
