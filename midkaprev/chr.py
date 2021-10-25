n = int(input())
alphabet = 'abcdefghjclmnopqrstyuvwxz'
commonchr = list()
myStr = list()
flag = True
for i in range(n):
    strings = input()
    myStr.append(strings)
for i in range(len(alphabet)):
    for j in range(len(myStr)):
        if alphabet[i] not in myStr[j]:
            flag = False
    
    if flag:
        commonchr.append(alphabet[i])
    flag = True 
print(*commonchr)       
