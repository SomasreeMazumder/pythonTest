class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()  # This start() function has no impact while completing this flight class


class AirbusEngine:
    def start(self):
        print("Starting the airbus")


class BoeingEngine:
    def start(self):
        print("Starting the Beoing")


ae = AirbusEngine()
f = Flight(ae)
f.startEngine()
be = BoeingEngine()
f = Flight(be)
f.startEngine()
