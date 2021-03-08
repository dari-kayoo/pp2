def uniqueList (*l):
    unList = []
    for i in l:
        if i not in unList:
            unList.append(i)
    return unList        
print(uniqueList(input().split()))            