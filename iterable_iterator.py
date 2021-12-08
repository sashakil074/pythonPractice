#. Write a Python program to print all characters of the word "Program" using iter and next
#functions. What will happen if you use next function for more than 7 times?

string="program"

itr=iter(string)

item=next(itr)
print(item)
item=next(itr)
print(item)
item=next(itr)
print(item)
item=next(itr)
print(item)
item=next(itr)
print(item)
item=next(itr)
print(item)
item=next(itr)
print(item)

#another next() function and we will get error: StopIteration

item=next(itr)
print(item)