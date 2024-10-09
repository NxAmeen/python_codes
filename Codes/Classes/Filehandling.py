file = open('zeeka.txt', 'r')
print(file.readline())


file = open('zeeka02.txt', 'w')
print(file.write('This is a new line'))

file = open('zeeka02.txt', 'a')
print(file.write('\nThis is an appended line'))
file.close()
print(file.closed)
print(file.mode)
print(file.name)



'''Rename a file'''
import os
os.rename('zeeka02.txt','zeeka01.txt')

'''or'''
import os
oldname = 'zeeka02.txt'
newname = 'zeeka01.txt'
os.rename(oldname,newname)


'''Delete a file'''
import os
if os.path.exists('zeeka01.txt'):
    os.remove('zeeka01.txt')
else:
    print('The file does not exist')
# os.remove('zeeka01.txt')
