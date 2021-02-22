import re
txt = 'Hello World'
x = re.search('^Hello.*World')
if x:
   print('YES! Is matched.')
else:
   prnt('NO!')
