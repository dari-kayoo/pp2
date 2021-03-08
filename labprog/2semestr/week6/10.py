sampleList = list(input().split())
resultList = []
for i in sampleList:
    if int(i)%2 == 0:
        resultList.append(i)
print(resultList)        
