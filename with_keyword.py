""""
1. Create a txt file manually on your Desktop with the name “info.txt”.
write 'hello python' inside it. After that:
a- Open the file using open function, read the content, insert the following line of
code, a = [1,2,3]; print(a[10]), close the file, and print the file status to know if it
is closed or not. Make sure to use try – except to make the program be executed
without any problem

"""

file_path=r'C:\Users\shaki\Desktop\Test\info2.txt'

try:
  fo=open(file_path,"r")
  tring = fo.read()
  a = [1, 2, 3]
  print(a[10])

  fo.close()
except:
  print("There is an error")
res = fo.closed
print('The file is closed:', res)


"""'
b- Open the file using open function with ‘with’ statement, read the content, insert 
the following line of code, a = [1,2,3]; print(a[10]) in the body of ‘with’, and 
print the file status out of with body to know if it is closed or not. Make sure to 
use try – except to make the program be executed without any problem
"""

with open(file_path,"r") as fo:
    try:
        string=fo.read()
        a = [1, 2, 3]
        print(a[10])

        fo.close()
    except:
        print("There is an error")
res=fo.closed
print('The file is closed:',res)