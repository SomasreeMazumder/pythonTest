s1="This is a game"

for i in range(len(s1)):
    print(s1[i], end=' ')

print(i)

for i in range(-1,-len(s1)-1,-1):
    print(s1[i], end=' ')

print()

for i in range(1,len(s1), 3):
    print(s1[i], end=' ')

print()

for x in s1:
    print(x, end=' ')
print()



i=-len(s1)#-13
while(i<=-1):
    print(i,":", s1[i])

    i+=1

print()