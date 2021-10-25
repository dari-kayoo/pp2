a, b = (int(i) for i in input().split())
for i in range(a, b):
    if i == 3**i:
        print(i, end = ' ')