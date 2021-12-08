
#1. Write a Python program to find those numbers which are divisible by 7 and multiple
#of 5, between 1500 and 2700 (both included).

i=1500
l=[]
while i<=2700:
    if i%7==0 and i%5==0:
        l.append(str(i))
    i=i+1
print(l)


# using for loop
nl = []
for x in range (1500, 2700):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print(nl)

#. Write a Python program to count the number of even and odd numbers from the
#following series, numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) #tuples
ec=0
oc=0
for i in numbers:
    if i%2==0:
        ec+=1
    else:
        oc+=1
print('Number of even numbers: ',ec)
print('Number of odd numbers: ',oc)


#3. Write a Python program that prints each item and its corresponding type from the following data_list.
#data_list = [1452, 11.23, 1+2j, True, (0, -1), [5, 12], {"class":'V', "section":'A'}]

data_list = [1452, 11.23, 1+2j, True, (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in data_list:
    print('Type of {} is {}'.format(i,type(i)))

#4. Write a Python program which prints the word 'hello' for 10 times using while loop
i=0

while i<=10:
    print('hello')
    i=i+1