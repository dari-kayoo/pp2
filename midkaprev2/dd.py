d = dict()
try:
    while True:
        name = input()
        if name in d:
            d[name]+=1
        else:
            d[name] = 1 
except:
    pass
result = []
for i in d:
    if d[i]%2 == 0:
        result.append(i)
result.sort()        
for i in result:
    print(i)                       