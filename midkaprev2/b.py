import re
string = input()
foundMatch = re.search(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_])', string) #or you can write \W
if foundMatch:
    print('Found a match!')
else:
    print('Not matched!')    