a = list(map(int, input().split()))
k = -1
for i in range(len(a)):
    if a[i] != 0:
        print(a[i], end=' ')
        k += 1
for k in range(len(a)-k-1):
    print('0', end=' ')
