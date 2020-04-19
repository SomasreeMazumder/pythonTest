def xSquare(x):
    return x*x
print(xSquare(5))

valueA=lambda x: x*5
print(valueA(5))

valueB=lambda a,b : a*b
print(valueB(2,5))

def funA(y):
    return lambda x: x*y
a=funA(5)
print(a)
print(a(10))

#Applying lamda fun to a List

#listA=[2,7,3,5,9]x

#output=[4,14,3,5,18]

def applytoList(listA,lambfun):#3
    return [lambfun(x) for x in listA]
listB=[2,7,3,5,9]
print(applytoList(listB,lambda x:x*2))
