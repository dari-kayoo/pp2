# formatting strings
name = 'Dariga'
age = 18
print('My name is ' + name + '. I\'m', age, 'years old', sep=' ')
print('My name is {}. I\'m {} years old'.format(name, age))
print('My name is ' + str(name) + '. I\'m ' + str(age) + ' years old')
print('My name is {n}. I\'m {a} years old'.format(n=name, a=age))
floatResult = 1000/7
print('{0:1.4f}'.format(floatResult))
print("""
{0:1.5f} {0:1.5f} {}
{0:1.5f} {0:1.5f} {} 
{0:1.5f} {0:1.5f} {} """.format(1.4587, 15.4578, 7.897415,
                                84.486551, 8461.741, 7.4785,
                                8.5413481, 5.6585, 4.2741513))
