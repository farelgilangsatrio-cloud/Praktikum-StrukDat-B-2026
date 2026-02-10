'''LIST'''
# List
dataList = ['aku', 'kamu', 'dia']
print(dataList)

# list item
print(dataList[1])

# Changeable
dataList = ['aku', 'kamu', 'dia', 'aku']
print(dataList)

# List Length
print(len(dataList))

# List Items - Data Types
dataList = ['aku', 'kamu', 'dia', 'aku']
dataList2 = [1, 2, 3]
dataList3 = [True, False, True]

datacampuran = ['aku', 1, True]

# type
print(type(datacampuran))

'''Access List Items'''
# Acces Items
print(dataList[1])

# Negative Indexing
print(dataList[-1])

# Range of Indexes
print(dataList[1:3])
print(dataList[:3])
print(dataList[1:])

# Range of Negative Indexes
print(dataList[-4:-1])
print(dataList[:-3])
print(dataList[-1:])

# Check if Item Exists
if 2 in dataList2:
    print('yes!')

dataList[1] = 'mereka'
print(dataList)

dataList[1:3] = 'mereka', 'kamu'
print(dataList)

dataList.insert(1,'kalian')
print(dataList)

datalist2 = ["sayang","mama"]
dataList.extend(datalist2)
print(dataList)

dataList.remove("mereka")
print(dataList)

dataList.pop(1)
print(dataList)

dataList.clear()
print(dataList)

'''Loop Lists'''
# Loop Through a List
strlist = ["apple", "banana", "cherry"]
for x in strlist:
    print(x)

# Loop Through the Index Numbers
for x in range(len(strlist)):
    print(x)

# Using a While Loop
i = 0
while i < len(strlist):
    print(strlist[i])
    i = i + 1

# Looping Using List Comprehension
[print(x) for x in strlist]

'''List Comprehension'''
buah = ["apple", "banana", "cherry", "kiwi", "mango"]
listbaru = []

for x in buah:
    if "a" in x:
        listbaru.append(x)
        print(x)

# The Syntax
listbaru = [x for x in buah if x != "apple"]
listbaru = [x for x in buah]

# Iterable
listbaru = [x for x in range(10)]

# Expression
listbaru = [x.upper() for x in buah]
nlistbaru= ['hello' for x in buah]
listbaru= [x if x != "banana" else "orange" for x in buah]

'''Sort Lists'''
# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

'''Copy Lists'''
# Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

'''Join Lists'''
# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)