#about List
someList = [1, 2, 3, 8]
print(someList[1])
anotherList = someList[:2]
print(anotherList)

#mutable
someList[2] = 'hi'
print(someList)
newList = anotherList + someList

#adding items
newList.append('item')
newList.insert(0, 'great')
print(newList)

#removing items
deletedItem = newList.pop(-1)

print(newList)
newList.pop(0)
print(newList)

print(deletedItem)
#removing with value = ничего не возращает: None
deletedIt = newList.remove(2)
print(deletedIt)

