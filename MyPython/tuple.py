# tuple is immutable!
tuple1 = 1, 2, 5  # you can write without brackets
tuple2 = ('hi', 'hello', 'me')
tuple3 = (3, 3.5, 85.47)

# tuple1[1] = 3  #this is error

newtuple = (tuple1[0], 3, tuple1[-1])  # or you can write [2]
print(newtuple)

print(tuple1[1])

print(type(tuple1))

print(tuple2)
print(tuple3)

personTuple = ('John', 'Smith', 1986)
firstName, lastName, yearOfBirth = personTuple
print(firstName, lastName, yearOfBirth)

x = y = 12
x, y, z = 4, 8, 45
print(x, y, z)

t1 = 1, 2, 2, 4, 78, 6
print(t1.count(2))
print(t1.index(2))
