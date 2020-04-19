class Bird:
    def __init__(self, a):
        print("Bird is ready to fly")
        self.a = a

    def whoisthis(self):
        print("Bird" + self.a)

    def swim(self):
        print("Swims Faster")


class Penguin(Bird):
    def __init__(self, a):
        super().__init__(a)
        print("Penguin can run faster")

    def whoisthis(self):
        print("This is penguin")

    def run(self):
        print("Can run")
        Bird.whoisthis(
            self)  # a good example of Method overriding as we can pass child's value inside this parent method
        b.whoisthis()


b = Bird("Cuckoo")
p = Penguin("Nightingle")
p.swim()  # inheretence
b.whoisthis()
b.swim()
p.whoisthis()
p.run()
