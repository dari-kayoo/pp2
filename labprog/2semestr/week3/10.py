n = int(input())
dictt = {}
for i in range(n):
    first, second = input().split()
    dictt[first] = second
    dictt[second] = first
word = input()
for i in dictt:
    if i == word:
        print(dictt[i])
        break    

