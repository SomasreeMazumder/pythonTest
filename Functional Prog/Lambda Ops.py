# CubeLambda:
# def cube(n):
#   return n**3
#   print(cube(2))
## Using Lambda:
a = lambda n: n ** 3
print(a(3))
print('***************************')
# Even or ODD :
l = lambda x: 'YES' if x % 2 == 0 else 'NO'
print(l(10))
print(l(9))

# Sum of 2 No.s
'''def add(a, b):
    return a + b


print(add(10, 20))'''
print("***********************")

l = lambda a, b: a + b
print(l(10, 20))
print("____________________________")
# Using a filter:(EVEN/ODD)
lst = [10, 3, 46, 19, 11, 78, 100, 51, 7]

even = list(filter(lambda x: x % 2 == 0,
                   lst))  #need to convert the field into
                          # list do list keyword is used else
                          #   it will give the memory loation
odd = list(filter(lambda x: x % 2 != 0, lst))
# print(even)
for i in even: print(i)
print(odd)
print("___________________________")
# Using Map Funtionts double the values of list:

lst = [2, 3, 4, 5]

result = list(map(lambda n: n * 2, lst))
print(result)
print("___________________________")

# Sum of all elements in a list:
from functools import reduce

lst1 = [5, 13, 15, 20]
resultofsum = reduce(lambda x, y: x + y, lst1)
print(resultofsum)
print("---------------------")
# Decorators double the numbers returned
def decor(fun):
    def inner():
        result = fun()#num()
        return result*2
    return inner()
def num(): #Decor
    return 5
resultfun = decor(num)
print(resultfun)
print("____________________________________")
#Decorating Strings:
def decorfun(fun):
    def inner(n):
        result = fun(n)
        result += "How are you?"
        return result
    return inner

@decorfun  #the parent decorfun is being called
def Hello(name):
    return 'Hello ' +name

print(Hello("Sanch "))
#print(decorfun(Hello("Sanch")))



