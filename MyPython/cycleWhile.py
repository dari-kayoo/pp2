x = 1

while x < 10:
    print(x)
    x += 2

x = 0
while x < 10:
    print(x ,' is less than 10')
    x += 1
else:
    print(x, ' is not less than 10')   

for x in range(10):
    print(x, ' is less than 10')     
else:
    x += 1
    print(x,' is not less than 10') 


#break, continue, pass

myList = [1, 2, 3]
for number in myList:
    #comment doesnt work to run this code without body of cycle
    pass   

print('Another code')

myList = [1, 2, 3]
for number in myList:
    if number == 2:
        break
    print(number)


print('Another code')

myList = [1, 2, 3]
for number in myList:
    if number == 2:
        continue
    print(number)


print('Another code')