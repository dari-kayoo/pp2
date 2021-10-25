def common(a, b, k):
    if b > a:
        a, b = b, a

    div = []    
    for c in range(2, b + 1):
        if b % c == 0 and a % c == 0:
            div.append(c)
    
    div.reverse()
    if not div:
        print(a)
    else:
        print(div[k-1])
            

a, b, k = (int(i) for i in input().split())
common(a, b, k)            