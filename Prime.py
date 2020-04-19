a=int(input())
i=1
for i in range(2,21):
    if a % i == 0:
        while a == i:
            pass
        print("the number is not prime" + str(i))
    else:
        print("the number is prime")