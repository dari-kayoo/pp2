# dictionary Comprehension
numberDict = {'first': 1, 'second': 2, 'third': 3}
newDict = {key: value**3 for key, value in numberDict.items()}
print(newDict)

numList = [6, -8, 87, -874, 47, 2, 47, -8, 0
           ]
nummDict = {num: num**2 for num in numList}
print(nummDict)
nummDict = {num: 'positive' if num > 0 else 'negative' if num <
            0 else 'zero' for num in numList}
print(nummDict)

#setComprehension
numList = [6, -8, 87, -874, 47, 2, 47, -8, 0
           ]
numSet = {num**2 for num in numList}
print(numSet)
numSet = {num**2 for num in range(2, 8)}
print(numSet)

letterSet = {letter.upper() for letter in 'hello'}
print(letterSet)
