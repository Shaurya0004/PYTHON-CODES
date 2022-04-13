# s = "Hello"
# w = "World"
# # and using concatenation we print hello world by using
# print(s+w)


"""
String formatting
In python we can do string formatting in multiple ways
"""

# ------------------------------

"""
Way no. 1-> using % operator
%s, %d, %f these are called format specifier 
%s -> string
%d -> integer
%f -> float
%b -> binary
%r -> boolean
"""

name = "Sanket"
year = 2021
happiness = 100.0
hm=True
greeting = "Hello, %s to %d and we hope your happiness matric is %f->%r" % (name, year, happiness,hm)
print(greeting)
'''
you have to remember one thing here that you have to take care of format also.Like if you have
 %f but in happiness variable you assign a string and not a float then it will show error.
 but if you enter a decimal in place of float or string in the given above case then it will work
 because decimal can be converted to both string and float but vice versa is not true.. 
'''
"""
Way no. 2-> using format function
"""
greeting = "Hello, {x}".format(x = name)
print(greeting)
greeting = "Hello, {x} to {y}".format( y = year, x = name)
print(greeting)
greeting = "Hello, {} to {} and we hope your happiness matric is {}".format(name, year, happiness)
print(greeting)
print(format(12, "b"))


"""
Way no. 3 -> F-strings
"""
binary = 0b101
greeting = f"Hello, {name} {~binary:0b}  to {year} and we hope your happiness matric is {happiness}"
print(greeting)