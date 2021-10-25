n = int(input())
a = [int(i) for i in input().split()]
newLIist = list(a)
newLIist.sort()
if a==newLIist:
    print('interesting') 
else:
    print('not interesting')
