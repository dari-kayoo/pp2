for x in range(3,10, 2): #in 1st we write from, in 2nd to, in 3rd our step 
    print(x)
print(range(5))
print(list(range(5)))   

 
letterIndex = 0
myString = 'abcdefg'
for letter in myString:
    print(letter + ' is at index ' + str(letterIndex))
    letterIndex+=1


#enumerate function
myString = 'abcdefg'
for letter, index in enumerate(myString):
    print(letter)

print('a' in 'Lady')
print('x' in 'Lady')
print(str(1) in 'Lady')
print('1' in 'Lady')

letteList = ['a', 'b', 'c', True]
print('a' in letteList)
print(1 in letteList)
print(True in letteList)

dict1 = {1 : 'a', 2 : 'b', 3:'c'}
print(1 in dict1)
print(1 in dict1.keys())
print('c' in dict1.values())

print(min(1, 3, 56, 4))
print(max(1, 3, 56, 4))

myList = [1, 3, 56, 4]
print(min(myList))

print(max('Hello'))

from random import shuffle

myList = [1, 2, 4, 56]

shuffle(myList)
print(myList)

from random import randint
print(randint(10, 100))