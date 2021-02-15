a = list(int(i) for i in input().split())
k = int(input())
k = k%len(a)

if k > 0:
    a = a[-k:]+[:-k]
else:
    k = abs(k)
    a = a[k:]+[:k]
prin(*a)    
