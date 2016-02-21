def binarySearch(alist, target):
	min = 0
	max = len(alist)
	mid = len(alist) // 2
	print (mid)

	while max - min != 1:
		if alist[mid] == target:
			return True
		elif alist[mid] < target:
			min = mid
			mid = ((max - min) // 2) + min
		else:
			max = mid
			mid = (max - min) // 2

	return False

print (binarySearch([1,2,4,5,6], 9))