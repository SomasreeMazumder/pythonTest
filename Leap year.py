def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # Write your logic here

#    if (year % 400 == 0 and year % 100 != 0):
#        print(True)
#    elif (year % 100 == 0):
#        return leap
#    if ((year % 4 == 0) or (year % 400 ==0) and (year%100!=0)):
#        print(True)
#    else:
#        return leap

year = int(input())
print(is_leap(year))
