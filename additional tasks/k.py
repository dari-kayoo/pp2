n = int(input())
h = n//60
if h >= 24:
    h = h%24
print(h, n%60, sep = ' ')