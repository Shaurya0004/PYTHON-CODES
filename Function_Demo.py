  
""" We will create some functions

Now in python we can create a function like this
def functionname (arguments<optional>):

	this will create a new block where you will write logic

	
	return value <optional statement>
return and def are keywords
How to call a function ??? -> just by wirting the name and passing arguments
"""

def euclidean_dist(x1, y1, x2, y2):
	"""
	this functions will calculate euclidean dist
	this is a docstring
	x1 (int): x coordinate of first point
	x2 (int): x coordinate of second point
	y1 (int): y coordinate of first point
	y1 (int): y coordinate of second point
	"""
	value = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
	"""
	This will be treated as a normal comment
	"""
	'''
a docstrng is written just after defining the function
and is displayed in the output to give information about
 your function for better understanding or you say that it is 
 written to explain the function like what are its inputs etc....   
you must remember that you have to write    print(euclidean_dist.__doc__)
to print the docstring also....
'''
	return value

def manhattan_dist(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)  #abs stands for mode 


def function_without_argument():
	print("No arguments")
	return 10

def function_without_return(x):
	y = x + 10

def function_without_argumentsandreturn():
	print("Welcome")

retval = euclidean_dist(12, 1, 0, 2) #so this is asking the function to 
# return a value  
print(retval)#this is printing that value.If return is not written then none will be 
# printed. you can try this by commenting that line no. 34.
print(euclidean_dist.__doc__)

print(manhattan_dist(y1 = 0, y2 = 0, x1 = -1, x2 = 2))

x = function_without_argument()
print(x)#this will print the value which is returned by that function which is 10 in this case
# you can also write print(function_without_argument()) 


function_without_return(10)
function_without_argumentsandreturn()