class Duck:
    def talk(self):
        print("Quack Quack")


class Human:
    def talk(self):
        print("Hello")


def CallTalk(obj):
    obj.talk()  # this talk() is no where associated with the Human class and Duck class


d = Duck()
CallTalk(d)
# pornhub(d)#this is for Duck
# d.talk()

h = Human()
CallTalk(h)  # this is for human
# h.talk()
