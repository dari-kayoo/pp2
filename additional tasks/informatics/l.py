n = int(input())
h = n//3600%24
m1 = n // 60 % 60 // 10
m = n//60%60
s1 = n%60//10
s = n%10
print(h, str(m1) + str(m), str(s1) + str(s), sep = ':')        