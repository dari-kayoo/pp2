import re
txt = input()
word = input()
x = re.search(word, txt)

if x:
    y = re.search(word,txt).start()
    print('First time ', word, ' occured in position:', y, sep = ' ')
else:
    print('Not found')    

