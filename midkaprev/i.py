n = int(input())
mylist = list(input().split())
k = int(input())
firstPart = mylist[:k]
secondPart = mylist[k:]
a = ''.join(firstPart)
b = ''.join(secondPart)
print(int(a)*int(b))
