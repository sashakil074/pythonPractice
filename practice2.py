#string functions
str=' python beginner to advance '
l=len(str)
print(l)

str1 = 'restart'
c=str1[0]

str2=str1.replace('r','#')
str2=c+str2.replace('#','',1)
print(str2)


string = " python, beginner to advance course "
s1 = string.strip(' python,')
print(s1)

s2=string.split(',')
print(s2)

s3=string.replace('advance','beginner')
print(s3)

s4=string.isspace()
print(s4)

s5=string.isdigit()
print(s5)

s6=string.islower()
print(s6)

s7=string.title()
print(s7)

s8=string.capitalize()
print(s8)

s9=string.count("course")
print(s9)

s10=string.upper()
print(s10)

s11=string.find('to')
print(s11)

s12=string.lower()
print(s12)