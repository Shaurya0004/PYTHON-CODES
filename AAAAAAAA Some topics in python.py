#Any and All operators in python 
"""
ANY OPERATOR-->> returns true if any of the items is true.returns false if empty or all are true.Any can be thought of as a sequence of OR operations on the provided iterables.

ALL OPERATOR-->>> returns true if all of the items are true or if the iterable is empty.All can be thought of as a sequence of AND operations on the provided iterables.

"""

"""
# This code explains how can we 
# use 'any' function on list 

list1 = []
list2 = []
  
# Index ranges from 1 to 10 to multiply
for i in range(1,11):
    list1.append(4*i) 
  
# Index to access the list2 is from 0 to 9
for i in range(0,10):
    list2.append(list1[i]%5==0)
  
print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))

"""

"""
# Illustration of 'all' function in python 3
  
# Take two lists 
list1=[]
list2=[]
  
# All numbers in list1 are in form: 4*i-3
for i  in range(1,21):
    list1.append(4*i-3)
  
# list2 stores info of odd numbers in list1
for i in range(0,20):
    list2.append(list1[i]%2==1)
  
print('See whether all numbers in list1 are odd =>')
print(all(list2))

"""

# difference between ==  and is in python

"""
== -->> this just check the value and not the address/id and returns true if the values are same.

is -->> this check value as well as id and returns true if both value and id are same of the two 

"""
# Python program to demonstrate list 
# comprehension in Python 
    
# below list contains square of all 
# odd numbers from range 1 to 10 
"""

odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square)

"""
