
# Introduce yourself using a python dictionary, where your dict should include your:
#name, age, specialty

dict={'name':'shakil','age':23,'speciality':'none'}

print(dict)
print(type(dict))

#. Check if the dictionary includes your "age"

res='age' in dict
print(res)


#c. What are the points (the dictionary keys) that have been covered when you
#introduced yourself?

res=dict.keys()
print(res)

#. Define a dictionary contains your favorite movie info ("name", "release_year",
# "director")

dict1={"name":"RRR","release_year":"2021","director":"Rajamouli"}

print(dict1)

#. Extract only your movie name

m_name=dict1.get("name")
print(m_name)

#Extract your movie info as a list of tuples
res=dict1.items()
print(res)

# Remove "release_year" from your dictionary

del dict1["release_year"]
print(dict1)

# Extract who is your movie director?

m_director=dict1.get("director")
print(m_director)

#Define a dictionary which describes a cat, where it should include : name, color, age

cat={'name':'Tommy','color':'Black','age':3}
print(cat)

#. Change your cat color to "white"

cat['color']='White'
print(cat)

#. How many items in your cat_dict?

res=len(cat)
print(res)

#  Extract your cat info (the dictionary values)
info=cat.values()
print(info)

#. Remove your cat color using pop () function

cat.pop('color')
print(cat)

#. Remove all items from your cat_dict

cat.clear()

print(cat)