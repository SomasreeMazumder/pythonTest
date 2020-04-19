'''
1)Dictionary is mutable datastrcture
2)dictioanry object
3)No indexing
4)keys and values
5)key and its bvalues are seperated by colon
6)key-value pairs are seperated by comma
7)keys must be immutable and unique
8)value pairs can be mutable or immutable
'''

# create an empty dictionary:

employess = {"1111": "James", "2222": "Lucy"}
print(employess)

# adding value
employess['3333'] = "Robert"
print(employess)

# modifying an existing value:
employess['1111'] = "Kelly"
print(employess)

print(employess['2222'])
# print(employess['4444'])#python throw error here
# accessing dictioanry elements using get function:
print(employess.get('1111'))
print(employess.get('4444'))

# loop through a dictionary
'''for <key> in <dict object>:
    statements
    statements
'''
for key in employess:
    print(key)
for key in employess:
    print(key, " : ", employess[key])
print(employess.keys())
for key in employess.keys():
    print(key)
# looping through dictioanry values:
print(employess.values())

for value in employess.values():
    print(value)
print(employess.items())

for item in employess.items():
    print(item)

for item in employess.items():
    print(item[0], " : ", item[1])

t1 = (3, 4)
#   0 1
print(t1[0])

# number of items in a dictioanry

print(len(employess))

# remove an element

del employess['3333']
print(employess)

key = '4444'
if key in employess:
    del employess[key]
print('1111' in employess)
print('4444' in employess)

# Number of Corona cases:
coronaData = {
    'Telengana': 100,
    'Maharastra': 400,
    'Kerala': 300,
    'Karnataka': 200
}

# Number of Corona cases and deaths:
coronaData = {
    'Telengana': [100, 2],
    'Maharastra': [400, 10],
    'Kerala': [300, 15],
    'Karnataka': [200, 5]
}

print(coronaData['Maharastra'])

print('Number of cases in Maharastra:', coronaData['Maharastra'][0])  ####
print('Number of  death cases in Maharastra:', coronaData['Maharastra'][1])  ####

for key in coronaData.keys():
    print(key, " : ", coronaData[key][1])
# update method:
student1 = {
    '101': ['James', 20, 'CSIS'],
    '201': ['Kalpana', '30', 'ECE']
}

student2 = {
    '401': ['Priyanka', 35, 'Management'],
    '501': ['Kishore', '25', 'civil']
}

student1.update(student2)
print(student1)

person = {
    'Name': "Zebra",
    'Height': 12 * 5 + 10
}
print('height of the person :', person['Height'])

grades = {
    'Smitha': [85, 94, 88],
    'Bhaskar': [86, 95, 78, 85]
}

print(grades['Smitha'])

# avergae grade for Smitha

x = sum(grades['Smitha'])
y = len(grades['Smitha'])

print('Avg grade for Smitha :', x / y)

# Nested Dictioary

employeeData = {
    'Name': {'First': 'sanjay', 'Last': 'Sukla'},
    'Jobtitle': ['Developer', 'MAnager'],
    'city': 'Pune',
    'Salary': 100000.00
}
print(employeeData['Name'])

print(employeeData.get('Name'))

print(employeeData['Name']['Last'])

print(employeeData['Name'].get('Last'))

print(employeeData['Jobtitle'].append('SystemAnalyst'))
print(employeeData['Jobtitle'])

a = {100: None}
print(a)

studentGrades = {
    ('Smitha', 'kolluri'): [85, 94, 88],
    ('Bhaskar', 'Tiwari'): [86, 95, 78, 85]
}

for key in employeeData:
    print(key)

