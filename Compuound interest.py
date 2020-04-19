
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

    print("%02d : %.2f" %(years, balance))

message = "The investment with the interest %.2f becomes double  with the principle to %.2f in %d years" %(interestAmount, balance, years)

print(message)