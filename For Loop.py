for i in range(10):
    print(i, end=' ')

print()

for i in range(5,10):
    print(i, end=' ')

print()

for i in range(5,15,3):
    print(i, end=' ')

print()



'''
#comaprison between while and for loop
1) Initialize a varible(i=5)
2) check the avariable(i < 15)
3)excute a statement (printing i)
4)increment/decrement the counter (i +=3)
5) go back tot step 2
'''

i=5
while (i<15):
    print(i, end=' ')
    i+=3

print()

#code to double the investment
#you invest certain amount for certain interest rate
#how long does it take for the the investment to be double

years =0
initialAmount= 100000
rateOfInterest=6.99

targetAmount = initialAmount*2

balance = initialAmount #running total

while(balance<=targetAmount):
    years +=1
    #calculate interest amount
    interestAmount=balance * rateOfInterest/100

    #update balalnce
    #this statemnent eventually changes the condition to false
    balance += interestAmount

    print("%4d : %.2f" %(years, balance))

message = "The investment with the interest %.2f becomes double to %.d in %d years" %(interestAmount, balance, years)

print(message)

'''
Nested loop
loop inside loop
to build a multiplication table
'''

for i in range (1,11): #1,2,...10
    for j in range (1,11):

        print("%4d" %(i *j), end=' ')

    print()

#break and Continue statement
#Break statment breaks out of the loop completely
i = 5
while (i<15):
    print(i, end=' ')

    if (i ==10):
        break
    i=i+1

numLst =[2,6,3,9,5,3,7]

total= 0
i=0

while(i< len(numLst)):
    if (numLst[i]==3):
        i+=1
        continue
    total+=numLst[i]
    print(i, " : ", total)
    i+=1

print()