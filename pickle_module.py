#1 Write a Python program to create a pickle file on your pc and write the sentence 'Hello Python'
#in this file, then read the content again

import pickle
import os



file_path=r'C:\Users\shaki\Desktop\Test\dummy_pickle.pkl'

with open(file_path,"wb") as f:
    s="Hello Python"
    pickle.dump(s,f)

with open(file_path,"rb") as f:
    s_pkl=pickle.load(f)
print(s_pkl)

""""
2 Write a Python program to create student_dict = {'name': 'Sarah', 'course': 'Python'}, and
then print the content in two cases:
a. After converting the object into pickle data
b. Original object after we convert back the pickle data into its original form

"""


student_dict = {'name': 'Sarah', 'course': 'Python'}
dict_pkl=pickle.dumps(student_dict)
print(dict_pkl)

dict_pkl2=pickle.loads(dict_pkl)
print(dict_pkl2)