numberList = [1, 57, 9, 17, 56]
letterList = ['a', 'k', 'w', 's', 'v', 'x']

numberList.sort()
letterList.sort()

print(numberList)
print(letterList)
# we cant write like x = letterList.sort() : we get not true answer!
newList = letterList
print(newList)
# then we take sorted list. only withthis way

# reverse
numberList.reverse()
letterList.reverse()

print(numberList)
print(letterList)

# list in the list!!!
numberList.append(letterList)
print(numberList)
