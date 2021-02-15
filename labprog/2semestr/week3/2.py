a = [int(i) for i in input().split()]  
mini = 10000
for i in range(len(a)):
    if(a[i] > 0):
        if(a[i] < mini):
            mini = a[i]
print(mini)        