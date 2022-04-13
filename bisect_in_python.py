import bisect

arr = [int(x) for x in input().split()]#for this to give
# correct answer we must be giving it a sorted list as input
#like [1,2,2,2,4,4,6,7,8,8,8]

while True:
	ch = input()
	if ch == 'l':
		x = int(input())
		print(bisect.bisect_left(arr, x)) # O(logn)
	elif ch == 'r':
		x = int(input())
		print(bisect.bisect_right(arr, x)) # O(logn)
	else:
		break