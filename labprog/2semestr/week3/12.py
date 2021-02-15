n = int(input())
d = {}
a = {}
for i in range(n-1):
    child, parent = input().split()
    d[child] = parent
    a[child] = 0
    a[parent] = 0
for i in d:
    s = i
    while s in d:
        s = d[s]
        a[i] += 1
for i in sorted(a):
    print(i, abs(a[i]))
