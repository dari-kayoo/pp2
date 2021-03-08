def myFunc1():
    x = 'me'

    def myFunc2():
        nonlocal x
        x = 'you'
    myFunc2()
    return x


print(myFunc1())
