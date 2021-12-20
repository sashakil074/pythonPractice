#1. Write a Python program to create a lambda function that adds 15 to the given number a that
#passed in as an argument. Call your function for a = 10

addition=lambda a:a+15

print(addition(10))

#2. Write a Python program to create a lambda function that multiplies the numbers x y, z
#assuming the default value of z is 4. Print the result in the following cases:

mul=lambda x,y,z=4:x*y*z

#a. x = 12, y = 4 and use z as a default argument z = 4

print(mul(12,4))

#b. x = 3, y = 9, z = 11
print(mul(3,9,11))


#3. Write a Python program to create a lambda function that finds the maximum of group
#numbers assuming that the function could accept any number of arguments.
#Print the result for following cases:

maxn=lambda *args:max(args)

#a. (10, -3, -4, 12)

print(maxn(10, -3, -4, 12))

#b. (-12, -13, -5, -3, -9)

print(maxn(-12, -13, -5, -3, -9))


#4. Write a Python program to create a lambda function that finds the minimum of group of
#numbers using **kwargs to make the function accept any number of keywords arguments.
#Print the result for the following group of numbers: (-12, -13, -5, -3)

minn=lambda **kwargs:min(kwargs.values())

print(minn(a=-12,b=-13,c=-5,d=-3))


#5. Write a Python program to calculate the square of all elements of the list num = [3, 5, 6, -
#10, 4.5] using lambda and map functions

sq=lambda x:x*x
res=map(sq,[3, 5, 6, -10, 4.5])
print(list(res))

#6. Write a python program to find the positive numbers in the list
#num = [3, 5, 6, -10, 4.5, -11, -25, 9] using lambda and filter function

pos=lambda x:x>0

res=filter(pos,[3, 5, 6, -10, 4.5, -11, -25, 9])
print(list(res))