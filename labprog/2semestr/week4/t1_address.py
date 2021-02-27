import re
file = open('raw.txt', 'r', encoding = "utf-8")
txt = file.read()
adr = r'\nВремя.+\n(?P<Address>.+)'
address = re.search(adr, txt).group('Address')
print(address)
file.close()