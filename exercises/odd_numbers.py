def odd_numbers(low, high):
	if low > high:
		return "The first argument is higher than the second."
	if type(low) == int or type(high) == int:
		return "Only integers are valid input"
	results = []
	for i in range(low, high + 1):
		if i % 2 != 0:
			results.append(i)
	return results