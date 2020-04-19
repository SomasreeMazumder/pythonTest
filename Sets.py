##Sets  -- Mutable Data Structure:
#Sets do not support indexing
#Sets cannot have duplictes, have to be unique, but can have objects of various types
#Sets are mutable
#set elements do not have any order

#Creating an empty set:
s1 = set()
print(s1)

#Creating a set with default values:

s2 = {1, 2.34, 8, 'A', 'Python', True}
print(s2)
s3 = {1, 2, 2, 'a', 5.78, 7.89, 'a'}
print(s3)

#Number of elements:
print(len(s3))

t4 = ('Ahmedabad', 'Kolkata', 'Bengaluru', 'Chennai')
s4 = set(t4)
print(s4)
l5 = [1,2,3,1,4.5,6,3,9]
s5 = set(l5)
print(s5)
s6 = set("Missisipi")
print(s6)

s7={1,6,2.25,4,5.46}
print("minimum of s7=", sum(s7))

#print(s7[3])#indexing not allow in sets

a =[1,2,3]
b= [3,4,5]
c=a+b
print(c)

#check if + operand works or not
setA=set(a)
setB=set(b)
#setC= setA+setB
#print(setC)# set does not support addtion. TypeError: unsupported operand type(s) for +: 'set' and 'set'

#adding elements to a set
s7.add('a')
s7.add('b')
s7.add('a')

print(s7)
#remove an elements
#s7.remove('c') # it will show a key error as pyhton internally maintains hashmap/ dictionary mechanism. as c is present so it will throw key error
print(s7)

if 'c' in s7:
    s7.remove('c')
print(4 in s7)
print(1 not in s7)

try:
    s7.remove('c')
except:
    print("Somwthing wrong")
print(s7)

s8={1,2,3}
s9={2,3,1}

print((s8==s9)) #print true as order does not matter
print(id(s8)==id(s9))

s10={2,8,3,1}
s10.pop()
print(s10)

s11={2,8,3,1}
s11.discard(2)
print(s11)

s11.discard(9) #it will not throw any error if the value does not exists where as remove throws error
print(s11)

s12={9,2,5,4,1,7}
print(s12)

sorted(s12)

#set operation:

s1={1,2,3}
s2={8,1,6,2,3,7}

print(s1.issubset(s2))
print(s2.issuperset(s1))

#Union of Sets
s1={1,2,3}
s2={3,5,8}
s3={7,4,5}

print(s1.union(s2))
print(s1.union(s2).union(s3))
print(s1| s2)
print(s1|s2|s3)

s4={1,2,3,4,5}
s5={3,5,8,9,12}
print(s4.intersection(s5))
print(s4 & s5)

#s4={1,2,3,4,5}
#s5={3,5,8,9,12}
print(s5.difference(s4)) #elements are in s5 not in s4
print(s5 - s4)

#symmetric Difference
#Elements that are in either set, but not in both

print(s5.symmetric_difference(s4))
print(s5^s4)
