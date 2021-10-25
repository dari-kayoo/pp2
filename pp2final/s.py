n = int(input())
a = list(map(int, input().split()))
mx = -1
for i in range(n):
    if mx < a[i]:
        mx = a[i]

for i in range(n):
    if a[i] == mx:
        print(1, end = ' ')
    else:
        print(0, end = ' ')