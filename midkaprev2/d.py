d = dict()
try:
    while True:
        name = input()
        if name in d:
            d[name] += 1
        else:
            d[name] = 1
except:
    pass
l_ans = []
for i in d:
    if d[i] % 2 == 0:
        l_ans.append(i)
l_ans.sort()
for i in l_ans:
    print(i)
