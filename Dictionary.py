"""
Dictionary stores elements in Key, Value form
In dictionary,keys can only be those quantities which are not mutable.
Values can be anything. 
"""

x = {"name": "Sanket", (100, 3): 22, "name": "LinkedIn", "nested_dict": {1: 3, 2: 4}}

print(x)
print(type(x))
# What will happen if we give two same keys ?????
# it will override the existing key's value
# so in printing also only the last repeated key value pair is printed.see code output for more clarity.

# given a key how to access values ???

print(x["name"], x[(100, 3)])

# dict are mutable

x["name"] = "Unacademy"
print(x)

# How to add a key value pair ???
x["location"] = "Bengaluru"

print(x)

# how we can delete a key value pair ?

del x[(100, 3)]

print(x)

# print(x["hello"])  ->this will give error as there is no keyword named as "hello"

print(x.get("querty"), x.get("location")) # get is another way to extract values where
# if you dont have a value in the first place then it will return None.here if you diretly
# use print(x["querty"]) then as it is not present in the dictionary then it will give an error.
# so basically get is used as instead of giving error it will print NONE if (for eg qwerty is not present .)
#also in .get(<we pass key here for which we want to find corresponding value>)
# if you want to delete everything from a dict ???
# x.clear()

print(x)

# what if we want to print all the keys????
k = x.keys()
print(k)
print(type(k))
# what if we want to print all the values ????
v = x.values()
print(v)

for i in k:    #this means that now it will choose elements one by one from this (which are chosen randomly
# in case of dictionary and in an ordered way in case of lists etc ...)
	print(i)#and now it will print these elements one by one till all the elements are printed...

# iterate on values
for i in v:
	print(i)

for i in k:#in this case same procedure as in the line 52 but!!! 
	print(x[i])#but here it will print the corresponding values to the keys chosen as now it is x[i] and not simply i....
'''
one more thing we should remember is that the-->>  get(<the key value>) function is
defined for dictionaries only...
'''
