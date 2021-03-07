# this is set of something, they are not ordered.

rainbow = {'red', 'blue', 'green'}
print(type(rainbow))
print(rainbow)
emtyset = set()
# another way it is dict
print(emtyset)
emtySet = {}
print(type(emtyset))

# list to set and tuple to set
numberList = {1, 2, 3, 4, 4, 4, 3}
textTuple = {'pop', 'hope', 'hell', 'hell', 'dimond'}

setFromList = set(numberList)
setFromTuple = set(textTuple)

# adding element to set
setFromList.add(154)
setFromTuple.add('why')
print(setFromList)
print(setFromTuple)

# deleting
poppedSet = setFromList.pop()
poppedTextSet = setFromTuple.pop()

removedNumberSet = setFromList.remove(4)
removedeTextSet = setFromTuple.remove('hell')

setFromTuple.discard('root')
setFromList.discard(4)

print(setFromList)
print(setFromTuple)
print(poppedSet)
print(poppedTextSet)
print(removedeTextSet)
print(removedNumberSet)
