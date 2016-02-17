dict = {
	     4: [1,32,32,3],
	     3: [3,2,1],
	     2: [2,1],
	     1: [0]
       }

def maxValue(adict):
	max = 0
	for key in adict:
		if max < len(adict[key]):
			max = len(adict[key])
	return max

print (maxValue(dict))

def countElements(adict):
	count = 0
	for key in adict:
		count += len(adict[key])
	return count

countElements(dict)

def find_max_min(num):
    min = num[0]
    max = num[0]
    count = len(num)
    for i in range(1, count):
        if min > num[i]:
            min = num[i]
        if max < num[i]:
            max = num[i]
    if min == max:
        return [count]
    return [min, max]