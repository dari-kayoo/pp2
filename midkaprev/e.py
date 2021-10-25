txt = input().split()
maxLength = 0
maxLenWord = ''
for i in txt:
    if maxLength < len(i):
        maxLenWord = i
        maxLength = len(i)
print(maxLenWord)
print(maxLength)
