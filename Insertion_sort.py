def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i] # this element will be now inserted to it's correct position
		j = i - 1 # because the right place of insertion will be on left
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
		print(arr)

	return

li = [5, 1, 1]

insertion_sort(li)

print(li)
#insertion sort is in place and stable.
#its time complexity is O(n**2),theta(n**2) and ohm(n)
#its space complexity is O(1)
#number of comparisons=O(n**2)
#number of swaps=O(n**2)