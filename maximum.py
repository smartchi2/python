def maximum_number(maximum):
	largest = 0
	for index in range(len(maximum)):
		largest = 0
		if maximum[index] > largest:
			largest = maximum[index]
	return largest

input(maximum_number([1, 2, 2, 2, 3]))
