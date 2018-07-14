style = {'color': 'red', 'age': 23}

for v in style.values():
    print(v)

for v in style.keys():
    print(v)

for v in style.items():
    print(v)

print()

for k, v in style.items():
    print('Key: ' + k + ' Value: ' + str(v))

if 'red' in style:
    print(True)
else:
    print(False)

message = 'It was a bright cold day in Apirl, and the clocks were striken thirteen'
count = {}

import pprint

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)
pprint.pprint(count)
