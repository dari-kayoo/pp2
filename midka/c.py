n = input().split()
s = set(n)
l = list(s)
cnt = 0
for i  in range(len(l)):
    t = n.count(l[i])
    for j in range(t):
        cnt+= j
print(cnt)        