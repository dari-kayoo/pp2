# carPrices = {'opel': 5000, 'toyoto': 7000, 'bmw': 10000}
# print(carPrices)
# #we take price of toyoto
# print(carPrices['toyoto'])
# #adding
# carPrices['mazda'] = 4000
# print(carPrices)
# #dictionaries key cannot be same
# carPrices['opel'] = 2000
# print(carPrices)# it change own value, not add new items
# #deleting
# del carPrices['toyoto']
# print(carPrices)
# #deleting all dictionary is:
# # del carPrices
# # print(carPrices) #this is error

# #this deleting is true
# carPrices.clear()
#print(carPrices)

person = {
    'first name' : 'Dariga',
    'last name' : 'Zhakysh',
    'age' : 18,
    'hobbies' : ['dancing', 'reading', 'sewing', 'playing volleyball'],
    'disciplines' : {'Wednesday' : 'English',
                     'Thursday' : 'Calculus',
                     'Friday' : 'Statistics'} 
}
print(person['age'])
print(person['hobbies'][2])
hobbies = person['hobbies']
print(hobbies[2])

disciplines = person['disciplines']
print(disciplines['Wednesday'])
print(person['disciplines']['Thursday'])
person['car'] = 'toyoto'
print(person)

person['hobbies'][0] = 'painting'
print(person['hobbies'])

print(person.keys())
print(person.values())
print(person.items())
