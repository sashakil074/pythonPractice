#1. Define a Python function to find the maximum number assuming that the function can
#accept any number of arguments. Use your function to calculate the maximum of the
#following passed numbers


def maximum(*args):
    m=args[0]
    for i in args:
        if i>m:
            m=i
    return m
#a. passed_numbers = (5, 6)
print(maximum(5,6))


#b. passed_numbers = (7, 6, 11, 22)

print(maximum(7, 6, 11, 22))

#c. passed_numbers = (4, 9, 34, 100, 67)
print(maximum(4, 9, 34, 100, 67))


#2. Define a Python function to print employee details. Use your function to print:

def employee(fname,lname,**kwargs):
    print(f'{fname} {lname} details are {kwargs}')

#a. first_name : ali, last_name : ali'
employee('ali','ali')

#. first_name : khaled, last_name : shaaban, specialty = Engineering

employee('khaled','shaaban',specialty = 'Engineering')

#. first_name : kamal, last_name : 'assad', age : 25

employee('kamal','assad',age = 25)