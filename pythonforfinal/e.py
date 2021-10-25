import re
address = input()

captain = re.search('^[a-z].*[@][a-z].*[.][a-z].*', address)
if captain:
    print('Yes')
else:
    print('No')