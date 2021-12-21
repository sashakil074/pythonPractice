import math
# Write a Python program to convert the list of strings
#colors = ['Red', 'Blue', 'Green', 'Black', 'White'] to a list of upper case strings

colors = ['Red', 'Blue', 'Green', 'Black', 'White']

res=[n.upper() for n in colors]
print(res)

#2. Write a Python program to create a list of numbers that are divisible by 6 in the range (0,100)

res=[n for n in range(0,100) if n%6==0]

print(res)

##3. Write a Python program to create a new list which contains square root of the given list
#items [16, -4, 49, 0, -9, 25, -36] in case it is possible, and 0 otherwise

list=[16, -4, 49, 0, -9, 25, -36]

list1=[math.sqrt(n) if n>=0 else 0 for n in list]

print(list1)

#4. Write a Python program to create a set containing only integers from the given
# list [19, 23, 45, 'a', 'b', 5, 'r']

list= [19, 23, 45, 'a', 'b', 5, 'r']

st={n for n in list if type(n)==int}
print(st)

"""
5. Write a Python program to create a dictionary from the given tuple
fruit = ("apple", "banana", "cherry")
where the key is the tuple element index, and the value is the element itself
"""
fruit = ("apple", "banana", "cherry")

dct={fruit.index(n):n for n in fruit}
print(dct)
