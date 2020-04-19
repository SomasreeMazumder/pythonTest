t1 = (1, 1.5, "Java", [4,8,2], True)
print(t1)
t1[3][1] = 'Python'
print(t1)

#Functions:
#Built-in Functions:

x = "Programming is fun!!"
print(x)
x = 4.5
print(type(x))

#Functions from other module:

import math
x= 5
print("Cube of x = ", math.pow(x,3))
#print("sqr8 of x = ", m.sqrt(x,2))
from math import sqrt
print("Square root of x = ", sqrt(x))

##User-defined Functions:
#Fn without any input/output:(nothing out of the fn)
def displayMessage():
    message = "COVID-19: Please stay home unless it's extremely important"

    print("=" * len(message))
    print(message)
    print('=' * len(message))
print(displayMessage())

##Compute average of a list of no's
#Fn accepts a list:
#Void functions:
def computeAvg(numList):

    count = len(numList)
    total = sum(numList)
    average = total/count
    print("Avderage = %.2f" %average)
computeAvg([2,3,4])  #call fn using anonymous list

computeAvg([1.2, 2.5, 4.3])

#Fn that accept and return values:

def computeFactorial(num):
    if (num == 0 or num == 1):
        num = 1
    else:
        num = num * computeFactorial(num-1)

    return num
x=int(input("Enter a number: "))
fact=computeFactorial(x)
print('Factorial of x = ',fact)

#function to return multiple values:

def findMinMax(numList): #1
    max=numList[0]
    min=numList[0]

    for num in numList:
        if num>max:
            max=num #replace maximum
    for num in numList:
        if num< min:
            min=num #Replace minimum
    return min, max

x,y=findMinMax([2,8,5])
print('Min and Max are',x,y)


#VAriable Scope:

num=5.6

def displayNumber(val):
    print("Local number:", val)

    print("Global number: ",num)

    # num=8.5
    # print("inside global :", num)



displayNumber(2.5)
print('global outside ' ,num)


def calint(p,r,t):
    i = p*r*t/100
    print("interest amt = %.2f" %i)

calint(1000,0.01,10)
calint(t = 20, p = 10000, r = 0.99)
calint(50000,r=5.5, t=30) #one more thing to notice that it can change the values in runtime


def calint(p=10000,r=0.01,t=10): #Giving default values to the paraeters
    i = p*r*t/100
    print("interest amt = %.2f" %i)

calint(p=1000,t=20)

def displayList(numList):
    print(id(numList))
    print(numList)
    numList[1]='Python'
    print(numList)
x=[1,2,3]
#y=x here address will be same
y=list(x)
print(id(y))
print(id(x))
displayList(x)

print(x)
print(y)


#passing varibale argument

def addNum(*nums): #it takes the unorganised dataset which are not belonging to any DataSctructure
    total=0
    for n in nums:
        total+=n
    return total
s=addNum(1,2)
print(s)