class Student:
    def __init__(self):
        self.__id='123'
        self.__name="ABC"

    def dispaly(self):
         print(self.__id)
         print(self.__name)


s= Student()

print(s._Student__id)
print(s._Student__name)
s.dispaly()
#print(s.id)
#print(s.name)