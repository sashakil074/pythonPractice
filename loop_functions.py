# Can you iterate over the string fruit = "Apple" while printing each letter with its index
fruit = "Apple"

for letter in enumerate(fruit):
    print(letter)


# 2. Write a Python program to perform sum of the number from 1 to 10, using range function

sum=0
for i in range(1,11,1):
    sum=sum+i
print(sum)

#3. Write a Python program to aggregate the following tuples together first_name, last_name,to get a full name as a result,
#first_name = ("John", "Charles", "Mike"),
#last_name = ("Jenny", "Christy", "Monica")

first_name = ("John", "Charles", "Mike")
last_name = ("Jenny", "Christy", "Monica")

for i,j in zip(first_name,last_name):
    print(i,'',j)

# Write a Python program to print all numbers from 0 to 5,
#and print a message when the loop ends

for i in range(6):
    print(i)
else:
    print('Finally finished!')
