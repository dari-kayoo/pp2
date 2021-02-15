a = input().split()
x = 0
for i in range(len(a)):
    if a[i]!= "0":
        print(a[i])
        x+=1
leng = len(a) - x        
for i in range(leng):
    print("0")        

          

