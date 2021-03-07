greeting = 'hello!'
letterList = []
for letter in greeting:
    letterList.append(letter)
print(letterList)

letterList = [letter for letter in greeting]
print(letterList)

numberList = [number for number in '156889']
print(numberList)

numberList1 = [num for num in range(5)]
print(numberList1)

numberList2 = [num**2 for num in range(5)]
print(numberList2)

numberList3 = [(num-3/2)**2 for num in range(5)]
print(numberList3)

myList = [1, -5, 78, -96, 45 , 98]
newList = [num for num in myList if num > 0]
print(newList)

newList1 = ['+' if num > 0 else '-' for num in myList]
print(newList1)