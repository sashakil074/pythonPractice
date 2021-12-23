""""
1. Manually: Create a folder with the name test, and create a txt file inside it with the name
'python'
Write a python program to:
a. Get your file name
b. Get your file directory(folder)
c. Get your file name and file directory
d. Get your file extension
e. Check if a file (‘course.txt’) is available inside your folder
f. Check if a directory (folder1) is available inside your folder
g. Create a path from your directory name and a file name
"""


import os

path=r'C:\Users\shaki\Desktop\Test\dummy.txt'

file_name=os.path.basename(path)

print(file_name)

dir_name=os.path.dirname(path)
print(dir_name)

dir_name,file_name=os.path.split(path)
print(file_name)
print(dir_name)

dir_name,file_ext=os.path.splitext(path)
print(file_ext)

path=r'C:\Users\shaki\Desktop\Test\course.txt'
res=os.path.isfile(path)
print(res)


path=r'C:\Users\shaki\Desktop\Test\folder1'
res2=os.path.isdir(path)
print(res2)

dir_name=r'C:\Users\shaki\Desktop\Test'
file_name=r'dummy.txt'

path=os.path.join(dir_name,file_name)
print(path)