import re
string = input()
foundMatch = re.search(r'[A-Z][a-z]', string)
if foundMatch:
    print('Found a match!')
else:
    print('Not matched!')    