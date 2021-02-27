import re
file = open('raw.txt', 'r', encoding = "utf-8")
txt = file.read()
numberOfBin = r'\nБИН.(?P<BIN>.+)'
numOfBin = re.search(numberOfBin, txt).group('BIN')
print(numOfBin)
file.close()