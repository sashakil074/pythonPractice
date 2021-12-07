#creating tuple

tup=('a','v','d')
print(tup)

#a Python program to get the 4th element from the beginning and 4th element
#from the end of the following tuple
tuple_y = ('h','e','l','l','o','p','y','t','h','o','n')

item1=tuple_y[3]
item2=tuple_y[-4]
print(item1)
print(item2)

# Python program to find the length of the following tuple.
tuple_x = (5, 10, 7, 4, 15, 3)

res=len(tuple_x)
print(res)

# Python program to define a new tuple from the tuple tu after repeating its
#elements three times: tu = (' a', ' v', ' d'), using tuple repetition operator.

tu = (' a', ' v', ' d')

tu*=3

print(tu)

""""Assume you have the tuples tu = (12, 30, 43, 22, -9, 4, 21, 44, 3), tu1 = ('a', ' v', ' d')
Write a Python program to:"""

tu = (12, 30, 43, 22, -9, 4, 21, 44, 3)
tu1 = ('a', ' v', ' d')
#Check whether the element 'a' exists in the tuple tu

res='a' in tu
print(res)

#. Find the maximum and minimum number in the tuple tu

maximum=max(tu)
minimum=min(tu)
print(maximum)
print(minimum)

#Create a new copy of tu which contains tu, tu1 using tuple concatenation and
#assign operator

new_tuple=tu+tu1
print(new_tuple)

#create a new tuple from tu, where it contains the last three elements of tu

new_tup=tu[-3:]
print(new_tup)