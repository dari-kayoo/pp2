f = open("perfect.in", "r")
a = f.read()
cnt =0
a1 = list()
for i in a:
   if i !="\n":
      cnt +=1
   else:
      a1.append(cnt)
      cnt = 0
print(a1)
a2 = list(a1)
a2.sort()
print(a2)
f1 = open("perfect.out", "w")
if a2==a1:
   f1.write("Yes")
else:
   f1.write("No")
f1.close()