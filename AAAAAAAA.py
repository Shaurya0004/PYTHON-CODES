#The count function..
a=[1,2,3,2,12,3,4,2,]
Set=set(a)
for i in Set:
	k=a.count(i)
	print('the number of times', i ,'comes is' , k)


#taking multiple inputs
''' if you want to take multiple inputs in a single 
    line from the user you can do this in the following
    way-->>  x =[int(x) for x in input().split()]  <<--
here you can also use float etc in place of int 

we can use round function to round-off the float value to 
desired decimal places
the function is round(float number,z) where z is the nuber of decimal
								places upto which you want to round off

