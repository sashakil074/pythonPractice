#old-style formatting
template="Date: %s, Time: %s, ATM NUMBER: %s, AMOUNT = %f $"

value1="07-12-21"
value2="18.22"
value3="NYO134"
value4=400.0

string=template % (value1,value2,value3,value4)
print(string)

#another ex
template="Date: %s, Time: %s, ATM NUMBER: %s, AMOUNT = %0.1f $"

value1="07-12-21"
value2="18.22"
value3="NYO134"
value4=400.0

string=template % (value1,value2,value3,value4)
print(string)


#string formatting using new style fomatting

template="Date: {}, Time: {}, ATM NUMBER: {}, AMOUNT = {} $"

value1="07-12-21"
value2="18.22"
value3="NYO134"
value4="400.0"

string=template.format(value1,value2,value3,value4)
print(string)