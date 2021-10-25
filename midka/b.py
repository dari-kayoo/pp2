string = input()
char = input()
pos = string.index(char)
myList = []
for i in range(len(string)):
    posi = pos - string.index(string[i])
    myList.append(abs(posi))
print(myList)    
