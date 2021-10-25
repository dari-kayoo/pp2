def odd(l, r):
    if(l> r):
        return
    
    print(l, end = ' ')
    if l%2 != 0:
        odd(l + 2, r)
    else:
        l+1
        odd(l+2, r) 

l, r = (int(i) for i in input().split())
odd(l, r)
