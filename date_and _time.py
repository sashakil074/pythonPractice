#1. Can you find the current date and time?


from datetime import time,date,datetime,timedelta
#from dateutil import tz

cur_date=datetime.now()
print(cur_date)


#. How old are you by days?

from datetime import date

b_date=datetime(1998,2,10)
cur_date=datetime.now()
delta=cur_date-b_date
res=delta.days
print(res,'days')

#3. What is the date before 90 days from now?

cur_date=datetime.now()
td=timedelta(days=90)
res=cur_date-td
print(res)


#4. A website allows people to use its services only if they are above 30 years,
#how to check if you are eligible to use that website?

v_birthday=str(input("Enter your birthday:"))

date_format = "%d-%m-%Y"
my_date=datetime.strptime(v_birthday,date_format)
year1=my_date.year
cur_date=datetime.now()
year2=cur_date.year

res=year2-year1

if int(res)>30:
    print('Welcome')
else:
    print('you are not eligible')


""""
5. Write a Python program which takes the following string
date_time = 'Jun 12 2013 5:30PM', converts the string into a datetime object, and then print
the result.
"""

date_time = 'Jun 12 2013 5:30PM'

res=datetime.strptime(date_time,'%b %d %Y %I:%M%p')
print(res)


""""
6. Write a Python program in which you define the following date
2015-07-15 19:39:04 as a datetime object, and then convert the object into a string object
"""

date_time = datetime(2015, 7, 15, 19, 39, 4)

res=datetime.strftime(datetime,'%d/%m/%Y %H-%M-%S')
print(res)


""""
7. Compute the difference between two datetimes objects, using relativedelta function
date1 (2009, 2, 3)
date2 (2012, 4, 6)
"""
from dateutil.relativedelta import relativedelta
date1=date(2009, 2, 3)
date2=date(2012, 4, 6)

res = relativedelta(date1, date2)
print(res)