

"""
1. Write a Python program that creates a generator which returns the following list items l1 =
[12, 34, 76, 89] divided by 100, and then extract the generator values using:
a. next function
b. for loop
"""

l1 = [12, 34, 76, 89]

gen=(n/100 for n in l1)

print(gen)

print('Using next function')
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('Using for loop')
gen=(n/100 for n in l1)
for item in gen:
    print(item)


#2. Write a Python program that creates a generator which returns even elements from the given
#tuple tu1 = (17, 40, 36, 7, 5, -20), and then extract the generator values using for loop

tu1 = (17, 40, 36, 7, 5, -20)

gen=(n for n in tu1 if n%2==0)

print('Even numbers:')
for item in gen:
    print(item)


#3. Write a Python program that creates a generator which returns even elements from the given
#tuple tu1 = (17, 40, 36, 7, 5, -20) and 0 otherwise, and then extract generator values using
#next function

tu1 = (17, 40, 36, 7, 5, -20)

gen=(n if n%2==0 else 0 for n in tu1)

print('Even numbers or 0:')
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))




#4. Write a Python program that defines a generator function which generates multiples of 5
#until the given numbers ‘num’. Use your generator for num=25

def gen_func(num):
    for i in range(num):
        if i%5==0:
            yield i

res=gen_func(25)

for item in res:
    print(item)
