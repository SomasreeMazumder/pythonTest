def customgen(x,y):
    while x<y:
        yield x
        x+=1
result =customgen(10,17)

print(result)
for i in result:
    print(i)