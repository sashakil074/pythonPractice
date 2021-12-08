#. Write a Python program which prints info about the older person between the following girl and boy dictionaries using the ternary operator:
#girl = {'name': 'Huda', 'age': 29}
#boy = {'name': 'Ali', 'age': 47}


girl = {'name': 'Huda', 'age': 29}
boy = {'name': 'Ali', 'age': 47}

string='boy is older than girl' if boy['age'] > girl['age'] else 'girl is older than boy'

print(string)