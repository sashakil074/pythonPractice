import copy

#Assume you have list_1 = [2, 6, 9, 21], write a Python program to:

list_1 = [2, 6, 9, 21]

#. Create list_2 where list_2 is a deep copy of list1

list_2=copy.deepcopy(list_1)
print('List_2 = ',list_2)

# Change the third element of lis_1 to 3

list_1[2]=3
print('List_1 = ',list_1)

#c. Reprint list_2

print('List_2 = ',list_2)

#. Is list_2 same to list_1

res=list_1 is list_2
print(res)

#Assume you have dic_1 = {'course': 'Python', 'level': 'beginner'}, write a Python program to:

dic_1 = {'course': 'Python', 'level': 'beginner'}
print('dic_1= ',dic_1)

#. Create dic_2 where dic_2 is a shallow copy of dic1.
dic_2=dic_1  #shallow copy

print('dic_2 = ',dic_2)

#. Change the value of level key to 'Advance' in dic_1

dic_1['level']='Advance'
print('dic_1 = ',dic_1)

# Reprint dic_2

print('dic_2 = ',dic_2)

#. Is dic_2 the same to dic_1
res=dic_1 is dic_2
print(res)
