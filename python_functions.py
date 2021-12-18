#1. Define a Python function to find the minimum of three numbers (3, 6, -5).

def min_num(x,y,z):
    if x<y and x<z:
        minnum=x
    elif y<x and y<z:
        minnum=y
    elif z<x and z<y:
        minnum=z
    return minnum

a=min_num(3,6,-5)
print(a)

#2. Define a Python function to find the average of the list l = [8, 2, 3, 0, 7] items.

def avg(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum/len(l)
l = [8, 2, 3, 0, 7]
a=avg(l)
print(a)

#. Define a Python function that takes the list [1, 2, 3, 3, 3, 3,9, 11, 9, 4, 5]
#and returns a new list containing unique elements of the first one

list=[1, 2, 3, 3, 3, 3,9, 11, 9, 4, 5]

def unique(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    return a
res=unique(list)
print(res)


#4. Define a Python function that prints the following variables values (first_name, last_name,
#full_name). The default values are last_name: smith and full_name: john smith

def print_name(fname='john',lname='smith'):
    print(f'first name is {fname}\nlast name is {lname}\nfull name is {fname} {lname}')
print_name()

#5. Redefine the function calculate_average mentioned in the question 2, and then add the
#following sentence as a documentation string to this function:
#This function is to find the average of a list of numbers

def avg(l):
    """
    This function is to find the average of a list of numbers
    """
    sum=0
    for i in l:
        sum=sum+i
    return sum/len(l)
l = [8, 2, 3, 0, 7]
a=avg(l)

help(avg)
print(a)