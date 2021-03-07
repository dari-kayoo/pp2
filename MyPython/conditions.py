x = 5

if x > 3:
    print(x, 'is greater than', 3, sep=' ')
    print("i'm happy!")

elif x < 3:
    print(x, 'is less than', 3, sep=' ')
else:
    print(x, 'is equal to', 3, sep=' ')


dayTime = 'afternoon'
if dayTime == 'morning':
    print('Monster is wake up')
elif dayTime == 'afternoon':
    print('Monster is walking')
elif dayTime == 'evening':
    print('Monster is eating')
elif dayTime == 'night':
    print('Monster is sleeping')
else:
    print('Monster is doing something')


x = 40
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
print('Some text')


userInput = input()
if userInput == 'hello':
    print('hello! Nice to meet you!')

# false: 0, emty string, None, emty objects
if '':
    print('Something')
