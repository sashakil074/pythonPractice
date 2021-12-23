""""
# Question
1. Write a Python program to:
a. Create a txt file with the name 'info ' on your Desktop
b. Write the following sentences inside your file:
 I live in KL
 KL is a great city
You have to visit KL at least one time in your life
c. Check if your file is readable
d. Read the content of your file
e. Read your file line by line
f. Append some personal info to your file, and read the new content. For example:
"I work as a Data Scientist"
g. Rename your file to 'personal_info ', and get your new file name

"""

file_path=r'C:\Users\shaki\Desktop\Test\info.txt'
fo=open(file_path,'w')
fo.write("I live in KL\nKL is a great city\nYou have to visit KL at least one time in your life")
fo.close()

fo=open(file_path,'r')
is_readable=fo.readable()
print(is_readable)

string=fo.read()
print(string)

print('string lines: ')
string_lines=fo.readlines()
for s in string_lines:
    print(s)

fo.close()

fo=open(file_path,'a')
fo.write("\nI work as a Data Scientist")
fo.close()

import os

file_path=r'C:\Users\shaki\Desktop\Test\info.txt'
new_file_path=r'C:\Users\shaki\Desktop\Test\personal_info.txt'
#os.rename(file_path,new_file_path)



""""
2. Create a folder manually on your Desktop with the name test and save the following 
image inside it with the name'python.png'. After that, write a Python program to:
a. Read that 'python.png' file in binary mode and print the data type that you read
b. Delete that file
"""

file_path=r'C:\Users\shaki\Desktop\Test\test\python.png'

fo=open(file_path,"rb")
file_content=fo.read()
res=type(file_content)
print(res)
print(file_content)
fo.close()