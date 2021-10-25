n = input()
flag = False
for i in range(len(n)):
    if n[i] == n[len(n)-i-1]:
        flag = True
    else:
        flag = False    

if flag:
    print('YES')
else:
    print('NO')
