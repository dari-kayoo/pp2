def diapozon(n, l, u):
    if n <= u and n >=l:
        return True
    else:
        return False
n = int(input())
l = int(input())
u = int(input())
print(diapozon(n, l, u))
