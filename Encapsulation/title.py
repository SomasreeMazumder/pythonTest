# !/bin/python3

'''
def solve(k):
    return "".join(k.title().)


s = input("i am giving ")
result = solve(s)
print(result + '\n')'''

s = input("abcd")

for x in s[:].split():
    s = s.replace(x, x.capitalize())
    # print(x)
    # print(x.capitalize())

    # s = s.replace(x, x.capitalize())
print(s)
