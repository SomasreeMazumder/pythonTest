age= int(input("Enter the age:"))

i=1
for i in range(age):
    i +=1
    if (i%2==0):
        #print("even number:")
        print("even number: %s" %i, end=' ')

    else:
        print("odd number: %s" %i)
        #print(i, end=' ')
print()