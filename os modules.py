""""

1. 1- Write a Python program to:
a. Create a folder with the name: my_name
b. Print your current directory
c. Change your current working directory to the folder you just created
d. Create other directories inside your folder: fplder1, folder2, folder3, folder4
e. Create a directory with the name 'images'
f. Rename the folder ‘images’ folder to 'photos'
g. Get a list of available folders in your directory
h. Remove the folder 'photos'
"""

import os


cwd=r'C:\Users\shaki\Desktop\Test'
os.chdir(cwd)
folder_path=r'my_name'
#os.mkdir(folder_path)

cwd1=os.getcwd()
print(cwd1)

chd=r'C:\Users\shaki\Desktop\Test\my_name'
os.chdir(chd)
cwd2=os.getcwd()
print(cwd2)

folder_path1=r'folder\folder1\folder2\folder3'
#os.makedirs(folder_path1)

folder_path2=r'images'
#os.mkdir(folder_path2)

#os.rename(r'C:\Users\shaki\Desktop\Test\my_name\images',r'C:\Users\shaki\Desktop\Test\my_name\photos')

res=os.listdir(r'C:\Users\shaki\Desktop\Test\my_name')
print(res)

cwd3=r'C:\Users\shaki\Desktop\Test\my_name'
os.chdir(cwd3)

folder_path3=r'photos'
#os.rmdir(folder_path3)