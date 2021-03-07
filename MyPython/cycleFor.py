numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numberList:
    print(str(number) + ' hola!')
    #print('hi')


for number in numberList:
    if number%2 == 0:
        print(number)
    else:
        print('hey!')    
listNumersSum = 0
for number in numberList:
    listNumersSum += number
print(listNumersSum)
greering = 'hello Python'
for letter in greering:
    if letter == 'o':
        print(letter)
    print('One more letter')   
tupleList = [{'a', 'b'}, {'c', 'd'}, {'e', 'f'}]
for item in tupleList:
    print(item)
for letter1, letter2 in tupleList:
    print(letter1, letter2)    

for letter1, letter2 in tupleList:
    print(letter1)   
    print(letter2) 

tupleList = [{'a', 'b', '1'}, {'c', 'd', '2'}, {'e', 'f', '3'}]
for letter1, letter2 , number in tupleList:
     print(letter1, letter2, number)      

dictionary = {'key1':'value1', 'key2': 'value2', 'key3' : 'value3'}
#key-value pairs  
for item in dictionary.items():
    print(item)  
#keys
for item in dictionary:
    print(item)   
for item in dictionary.keys():
    print(item)
for key, value in dictionary.items():
    print(key)    
#values
for item in dictionary.values():
    print(item)
for key, value in dictionary.items():
    print(value)  
for _ in range(5):
    print('hello')