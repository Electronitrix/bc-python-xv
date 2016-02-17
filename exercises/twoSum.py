def twoSum1(alist, target):
	for i in range(len(alist)):
		for j in range(i + 1, len(alist)):
			if alist[i] + alist[j] == target and alist[i] != alist[j]:
				return [i, j]

def twoSum(alist, target):
	mapping = {}
	count = range(len(alist))
	for i in count:
		diff = target - alist[i]
		if diff not in mapping:
			mapping[alist[i]] = i
		else:
		    return [mapping[diff], i]	 

#print (twoSum([1,2,3,4,5], 8))
#print (twoSumOptimized([1,2,3,4,5], 8))