#list of states in India
#Mutable Objects - Lists:
listA = [2.3, 4, 67, 12.8, "Python", True]
for i in range(len(listA)):
    print(listA[i], end=' ')
print()

for i in range(-1, -len(listA)-1, -1):
    print(listA[i], end=' ')
print()

tupA = tuple(listA)
print(tupA)

#List Comprehension:

listB = [x for x in range(10)]
print(listB)

listC = []
for x in range(10):
    listC.append(x)
print(listC)
listD = [x*2 for x in range(5)]  #0,1,2,3,4
print(listD)

listE = [1/x for x in range(2,10)]   #2,3,....9
print(listE)

listF = [x/4 for x in listB]
print(listF)

listG = [x for x in listF if 0.5 <= x <= 1.25]
print((listG))

listH = []
for x in listF:
    if (0.5 <= x <= 1.25):
        listH.append(x)

print(listH)
#Using Nested Loop
# x=2, y= 1,2,3  3,4,5
# X = 3, y= 1,2,3 4,5,6
# x = 4, y =1,2,3 5,6,7

listI = []
for x in range(2,5):
    for y in range(1,4):

        listI.append((x+y))
print(listI)

listJ = [x+y for x in range(2,5) for y in range(1,4)]
print(listJ)

a = ['a', 'b', 'c']
b = ['x', 'y', 'z']
listK = [i + j for i in a for j in b]
print(listK)

listL = []
for i in a:
    for j in b:
        listl.append(i+j)

print(listL)




