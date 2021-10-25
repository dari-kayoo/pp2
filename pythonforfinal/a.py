n =int(input())
m = int(input())
k = int(input())

flag = False
for i in range(n, n*(m-1), n):
    if i == k:
        flag = True
for i in range(m, m*(n-1), m):
    if i == k:
        flag = True


if flag:
    print("YES")
else:
    print("NO")    
          