n = int(input())
string = input()
alphabet = 'ABCDEFGHIJKCLMNOPQRSTYUVWXZ'
newStr = ''
for i in string:
    a = (alphabet.index(i)+n) % 26
    newStr += alphabet[a]

print(newStr)
