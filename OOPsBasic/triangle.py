n = int(input("enter the number"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print()
print()
for i in range(1, n + 1):
    print("* " * (n - i), end='')
    print()
print()
for i in range(1, n + 1):
    print(" " * (n - i), end='')
    print(("* " * i), end='')
    print()
print()

lst = [10, 5, 7, 10, 12]
y = list(filter(lambda x: x % 2 == 0, lst))
