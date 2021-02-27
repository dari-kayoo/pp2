import re
file = open('raw.txt', 'r', encoding = "utf-8")
txt = file.read()
nameOfCompany = r'\nФилиал.(?P<Company>.+)'
nameOfTheCompany = re.search(nameOfCompany, txt).group('Company')

print(nameOfTheCompany)
file.close()
