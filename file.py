
# helloFile = open('ginf.csv')
# helloFileContent = helloFile.readlines()
# # for filename in helloFile:
# #     print(filename)
# print(helloFileContent)

# baconFile = open('bacon.txt', 'w')
# baconFile.write('Fried Rice\n')
# baconFile.close()
# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable')
# baconFile = open('bacon.txt')
# baconFile.close()
# content = baconFile.read()
# baconFile.close()
# print(content)

#
# import shelve
#
# shelfile = shelve.open('mydata')
# cats = ['sophie', 'pooka', 'simon']
# shelfile['cats'] = cats
# shelfile.close()

# input = input("Enter yes or no =>> ")
# linput = input.lower()
# print(linput)
#
# # if input == 'yes':
# #     print(True)
# # else:
# #     print(False)

dataset = open('newdata.txt', 'a')
dataset.write('\nIt\'s good to exercise')
dataset.close()
dataset = open('newdata.txt')
content = dataset.read()
print(content)
dataset.close()

