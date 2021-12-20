import math
"""
1. - Define a python function “multiply” to multiply all list items by 2.
- Define a python function “divide” to divide all list items by 2.
- Define a Python function “process” that accepts two parameters (a function and a
list). Inside the function “process”, call the function for the list and return the
result.
- Use your functions for the following list list1=[12, 13, 14]
"""
import math


def multiply(list):
    list1=[]
    for i in list:
        list1.append(i*2)
    return list1
def divide(list):
    list1=[]
    for i in list:
        list1.append(i/2)
    return list1

def process(func,list):
    res=func(list)
    return res

#a. To multiply the list items by 2
#b. To divide the list items by 2
x1=[12, 13, 14]
x2=[12, 13, 14]
print(process(multiply,x1))
print(process(divide,x2))


"""
2. Define a Python function ‘course_details’ that takes one parameter ‘title’ and returns one 
of the following two functions according to the ‘title’ value : ‘python_beginner’ or 
‘python_advance’. Each one of these functions should print some details about the 
related course

a. course1 = 'Python advance'
details: 'In this course we dive deeply in more complex topics using Python'
b. course2 = 'Python beginner'
details: 'This course gives you Python basics'
"""

def course_details(title):
    def python_beginner():
        print('This course gives you Python basics')

    def python_advance():
        print('In this course we dive deeply in more complex topics using Python')

    if title=='python_beginner':
        return python_beginner()
    if title=='python_advance':
        return python_advance()

course1=course_details('python_beginner')
course2=course_details('python_advance')


"""
3. - Define a python function that calculates the square root of a number ‘a’
- Define a decorator that improves the previous function by printing the following 
message ‘no sqrt for negative number’ when the passed number is less than zero
- Test your decorated function for the following two cases:
a. -25
b. 25
"""


def decorator(func):
    def wrapper(a):
        if a>=0:
            return func(a)
        else:
            print('no sqrt for negative number')
            return None
    return wrapper

@decorator
def sqrt1(a):
    return math.sqrt(a)

res1=sqrt1(-25)
res2=sqrt1(25)
print(res1)
print(res2)


"""
4. - Define a function ‘task’ that returns the value of 6
- Define two decorators. The first one ‘multiply’ multiplies the returned value of 
‘task’ by 3, and the second one ‘divide’ divides the value of ‘task’ by 2
a. Use each one of the decorators individually
b. Use both decorators together taking into account that multiplication should be 
executed before division
"""

def multiply1(func):
    def wrapper():
        x=func()
        return x*3
    return wrapper

def divide1(func):
    def wrapper():
        x = func()
        return x/2
    return wrapper




#a. Use each one of the decorators individually

@multiply1
def task():
    return 6

res1=task()
print(res1)

@divide1
def task():
    return 6

res2=task()
print(res2)

#b. Use both decorators together taking into account that multiplication should be
#executed before division

@multiply1
@divide1
def task():
    return 6

res=task()
print(res)