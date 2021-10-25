import re
txt = input()
t = input()
s = input()
f = input()
tToS = re.sub(t, s, txt)
print(tToS)

numOfSubstr = re.findall(f, tToS)
print(numOfSubstr)

