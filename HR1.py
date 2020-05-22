'''
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''
####################################################

'''
n = int(input("Please provide a number:"))
i = 1
for i in range(25):
    if (2 <= n <= 5) & (n % 2 == 0):
            print("Not Weird!!")
    elif (6 <= n <= 20) & (n % 2 == 0):
        print("Weird!!!")
    elif n > 20:
        print("Not Weird...")

    else:
        print("Odd Number.")
    i=i+1
print()
'''
n = int(input("Please provide a number:"))
if(n%2!=0):
    print('Weird')
elif(1 <= n <= 5) & (n % 2 == 0):
    print('Not Weird')
elif(6 <= n <= 20) & (n % 2 == 0):
    print('Weird')
elif (20<n) & (n % 2 == 0):
    print('Not Weird')

'''Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''

a = int(input("Input 1st no: "))
b = int(input("Input 2nd no: "))
sum = a+b
print(sum)
min = a-b
print(min)
mul = a*b
print(mul)

'''Read two integers and print two lines. The first line should contain integer division,  a//b . The second line should contain float division,  a/b .

You don't need to perform any rounding or formatting operations.'''

a = int(input())
b = int(input())
c = a//b
print(c)
d = a/b
print("%.3f"%d)




