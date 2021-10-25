way = 109
v = int(input())
t = int(input())
s = v*t
if s > 0:
    x = abs(s - way)
else:
    x = abs(s + way)  
if x >= 109:
    x = x%109    
print(x)