n = int(input())
a = [int(i) for i in input().split()]
if sum(a) >= 1:
    print('Clean:', 0)
    print('Dirty:', n)
else:
    print('Clean:', n)
    print('Dirty:', 0)
