""""
1. Write a Python Program to:
a. Define a function that defines and prints the variable s = "I love Python!", and then
try to print the same variable s out of the function, Is there any error and why?
b. Define a function that print a variable s before assignment and see the errors
"""

def func1():
    s="I love Python!"
    print(s)
func1()
print(s)

def func2():
    print(s)
    s="I love Python!"
    print(s)
func2()
