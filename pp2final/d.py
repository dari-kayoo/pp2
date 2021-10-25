a = list(map(str, input().split()))
words = []

for i in a:
    flag = True
    for j in range(len(i)):
        if i[j] != i[len(i)-j-1]:
            flag = False
    if flag == False:
        words.append(i)
words = set(words) 
words = list(words)       
words.sort()        
for i in range(len(words)):
    print(words[i])
