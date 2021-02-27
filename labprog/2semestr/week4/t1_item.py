import re
file = open('raw.txt', 'r', encoding = "utf-8")
txt = file.read()
unitPrice = r'\n(?P<title>.+)\n(?P<Count>.+)x(?P<unitPrice>.+)\n(?P<totalPrice>.+)\nСтоимость.\n(?P<Price>.+)'
unPrice = re.compile(unitPrice)
item = []
for i in re.finditer(unPrice, txt):
    item.append(i.group('title'), i.group('Count'), i.group('unitPrice'), i.group('totalPrice'))
for i in item:
    print(i)    
file.close()
