a = [int(i) for i in input().split()]
k = int(input())
k = abs(k)
x = 0
for i in range(k-1, len(a)):
    print(a[i])
    x += 1
leng = len(a) - x
for i in range(leng):
    print(a[i])
