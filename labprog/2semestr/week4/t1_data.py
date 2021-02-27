import re
file = open('raw.txt', 'r', encoding = "utf-8")
txt = file.read()
d = r'\nВремя:.(?P<Data>.+)'
data = re.search(d, txt).group('Data')
print(data)
file.close()