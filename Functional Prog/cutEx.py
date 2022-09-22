class A(Exception):
    def __init__(self, msg):
        self.msg = msg


def withdraw(m):
    print(m)
    if 50 < m:
        print(m)
        raise A("Value needs to be greater")


withdraw(60)
