string = input()
numOfUpperCaseLetter = 0
numOfLowerCaseLetter = 0
for letter in string:
    if letter.islower():
        numOfLowerCaseLetter += 1
    if letter.isupper():
        numOfUpperCaseLetter += 1

print('Upper case characters: ' + str(numOfUpperCaseLetter))
print('Lower case characters: ' + str(numOfLowerCaseLetter))
