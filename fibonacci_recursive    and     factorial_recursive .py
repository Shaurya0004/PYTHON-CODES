def fib(n):
	if n == 0 or n == 1: # base case
		return n

	a1 = fib(n-1) # assume this is correct value of n-1th fib
	a2 = fib(n-2) # assume this is correct value of n-2th fib

	ans = a1 + a2 # self work is to add
	return ans

print(fib(3))



def fact(n):
	if n == 1: # base case
		return 1

	value = fact(n - 1) # assume this works correctly
	ans = n * value # self work ans -> f(n)
	return ans


print(fact(4))