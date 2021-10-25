from itertools import permutations 
a = input()
b = input()
listOfb = []
perm = permutations(a) 

print(type(perm))
flag = False
for i in list(perm): 
    if i == listOfb:
        flag = True

if flag:
    print('YES')
else:
    print('NO')