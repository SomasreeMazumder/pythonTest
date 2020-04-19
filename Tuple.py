tup = ("oranges", "apples", "bananas")
print(tup)
#tup[0] = "cherries"
print(tup)
print(tup[0])
tup1=(1,2)
tup2=(3,4)
tup3=tup1+tup2
print(tup3)
del tup1

print(tup2)

list1=[1,45,100,20,10]
for i in list1:
   print(i)
print(list1)

for k in range(0,51,5):
    pass
##Nested for -Range
for i in range (0,5):
    for j in range(0,3):
        print(i*j)

##While Loop -- break

c = 0
while c < 5:
    c = c + 1
    #print(c)
    if c == 5:
        continue
    print(c)
#pass

c = 0
while c < 5:
    c = c+1
    if c == 3:
        pass
    print("******************")
    print(c)


#Tuple is immutable
#List is mutable
aTuple=(1,1.5,'COVID-19','Python', True)
print(type(aTuple))
print(len(aTuple))
print(aTuple[-3])
print(aTuple[-1])
print(type(aTuple[-1]))
print(aTuple[0:3])
print(aTuple[3:])
print(aTuple[:2])
print()
t1=('a','b',3,'d')
t2=(5,6)

t=t1+t2
print(t)
t3 = ('a',2)
print(t3*3) #Repitition Operator

for i in range(len(aTuple)):
    print (aTuple[i])
for item in range(len(aTuple)):
    print(item)

t5 = (1, 5.3, 'Java', [4, 8, 1, 2], True)
print(t5)
print(id(t5))
print(id(t5[2]))
print(t5[-2][1])
t5[-2][1] = "Python"
print(t5)

#list of states in India