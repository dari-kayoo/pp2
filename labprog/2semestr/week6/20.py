def nonLocalVariable():
    a = 0
    b = '0'
    print(a+int(b))
print(nonLocalVariable.__code__.co_nlocals)    