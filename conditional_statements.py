#Write a Python program that tells you if your new email address is available to be used or not.
#used_emails = ['student1@gmail.com', 'student2@gmail.com', ‘student6@gmail.com']
#new_email = 'student6@gmail.com'

used_emails = ['student1@gmail.com', 'student2@gmail.com', 'student6@gmail.com']
new_email = 'student6@gmail.com'

if new_email in used_emails:
    print('your new email is used before')
else:
    print('You can use your new email')

#. Create a calculator supporting the main four arithmetic operators (+, -, /, *)
#The user should enter two operands and the operator symbol. After that, the calculator
#should be able to identify the operator and print the result after calculation.

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))

op=input('Enter the arithmatic operation to be calculated:')

if op == '+':
    sum=a+b
elif op == '-':
    sum=a-b
elif op == '*':
    sum=a*b
elif op== '/':
    sum=a/b
elif op == '%':
    sum=a%b

print(op,'of the two number is: ',sum)
