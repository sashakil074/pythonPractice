# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

i=0
for  i in range(0,6) :
    if i == 3 or i==6:
        continue
    print(i, end=' ')
    i = i + 1

print("\n")

#2. Write a Python program that prints all items in available_names list and stop when the name = "ali" appears
#available_names = ['samer', 'sarah', 'ali', 'ashraf']

available_names = ['samer', 'sarah', 'ali', 'ashraf']

for i in available_names:
    if i=='ali':
        break
    print(i)

#Write a Python program to print the variable’s value and stop when the variable is equal to
#6 using while loop (The loop condition is variable > 0). Make sure to reduce the variable by 1 in each iteration
#variable = 15

variable = 15

while variable>0:
    if variable==6:
        break
    print('Current variable value :',variable)
    variable=variable-1

print("\n")
#Write a Python program to print the variable’s value except the value 6 using while loop
#(The loop condition is variable > 0). Make sure to reduce the variable by 1 in each iteration
#variable = 15

variable = 15

while variable > 0:
    variable=variable-1
    if variable==6:
        continue
    print('Current variable value :',variable)


