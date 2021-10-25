n = int(input())
a = set(map(int, input().split()))
l = list(a)
l.sort()
index = []
for i in range(1, len(l)+1):
   index.append(i)
ans = zip(index, l)
for item in ans:
   print(*item)
