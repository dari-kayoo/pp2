nestedlist = [[1, 2, 3, 5], [4, 5, 6], [5, 7, 8, 9]]
print(nestedlist)
print(len(nestedlist))
print(len(nestedlist[-1]))#from back find
print(nestedlist[0][3])

#get number 7
print(nestedlist[2][1])

#print nested list
for innerList in nestedlist:
    print(innerList)

for innerList in nestedlist:
    for num in innerList:
        print(num)

# do it by using list comprehension        
[[print(num) for num in innerList] for innerList in nestedlist]        
