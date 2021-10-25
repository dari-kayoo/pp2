n = int(input())
arr = list(input().split())
arrSet = set(arr)
if len(arr) == len(arrSet):
    print('YES')
else:
    print('NO')    
