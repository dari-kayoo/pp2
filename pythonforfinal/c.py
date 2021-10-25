a, b = (int(i) for i in input().split())
c, d = (int(i) for i in input().split())

if a+d > b+c:
    print('Barsenal')
    print(a+d, b+c, sep = ' ')
elif a+d < b+c:
    print('Arselona') 
    print(a+d, b+c, sep = ' ')   
elif a+d == b+c:
    if a == c and b == d:
        print('Frienship')
        print(a+d, b+c, sep = ' ')
    elif b > d:
        print('Areselona')    
        print(a+d, b+c, sep = ' ')
    elif d > b:
        print('Barsenal')
        print(a+d, b+c, sep = ' ')    