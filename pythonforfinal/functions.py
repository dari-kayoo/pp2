n = int(input())
def pluss(n):
    new = 1 + 3 
    new2 = 1 + 5
    if n < 0:
        return False
    if n == 1:
        return True
    elif new == n:
        return True
    elif new2 == n:
        return True   
    else:
        return(pluss(n-3) or pluss(n-5))
if pluss(n):
    print('YES')
else:
    print('NO')