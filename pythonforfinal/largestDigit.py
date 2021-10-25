n = int(input())
mx = 0
l = list()
while n:
    l.append(n%10)
    n/10 

l.sort()
mx = l[0]

print(mx)