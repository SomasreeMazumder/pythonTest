day = str(input("Enter day:"))
if day == "Tuesday":
    print("Today is Sunny")
else:
    print("Today it will rain")

print()

################################

weight = int(input("Current weight is : "))
#weightm=weight/6
i = 1
for i in range(10):
    i+=1
    weightm = weight / 6
    print("Current year:%d and weight on earth : %.10f and w8 into moon: %.4f" %(i, weight, weightm))
    weight += 1
    #weight = weight/6
    #print( "year: %d Weight in Moon : %.10f" %(i,weight))
    #weight += 1
print()
