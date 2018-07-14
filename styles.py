import Debs_fs


import os
# path = os.path.join('usr', 'bin', 'spam')
# print(path)

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('c:\\users\\jerry', filename))

cwd = os.getcwd()
print(cwd)

os.chdir('c:\\windows\\system32')
cwd = os.getcwd()
print(cwd)

# os.mkdir('c:\\users\jerry\\testz')
print(os.path.join('c:\\users\\jerry\\testz'))

totalSize = 0
os.chdir('c:\\windows\\system32')
for filename in os.listdir('c:\\windows\\system32'):
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\windows\\system32', filename))

print(totalSize)
