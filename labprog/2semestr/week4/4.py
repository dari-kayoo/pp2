import re
txt = "The rain in Spain"
d = re.search('\\s', txt)
print("The first white-space character is located in position:", d.start())