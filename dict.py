# mycat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
#
# # Dictionary keys and values
# # print(mycat['size'])
#
# print('my cat has ' + mycat['color'] + ' fur')
#
# birthdays = {'Alice': 'April 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#         print('Happy birthday ' + name)
#     else:
#         print("I do not have birthday information for " + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated')


# country = {'Nigeria': 'Abuja', 'Ghana': 'Accra', 'South Africa': 'Pretoria', 'Egypt': 'Cairo', 'Morocco': 'Dakar'}
# print(country.values())
#
# name = input("Pls Enter a country : ")
# if name in country:
#     print('The capital of ' + name + ' is ' + country[name])
# else:
#     print('We could not find ' + name + ' in our database')

import shelve


# bday_shelve = shelve.open('bdayShelve')
birthdays = {'Alice': 'April 12', 'Tolani': 'Jan 22', 'Cynthia': 'June 4'}

# bday_shelve['birthdays'] = birthdays
# bday_shelve.close()
#
# print(bday_shelve)
data = open('bday.txt', 'w')
data.write(birthdays)
data.close()
