from collections import Counter
n = int(input())
d = {}
for i in range(n):
    name, day = input().split()
    d[name] = day

coun = Counter(d.values())
print(dict(coun))

