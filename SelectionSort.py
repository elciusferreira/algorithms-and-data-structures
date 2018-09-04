def selection_sort(numbers):
	for i in range(len(numbers)):   # loop through numbers list
		min_idx = i   # set first number as smaller

		# loop through numbers list starting from the subsequent number
		for j in range(i+1, len(numbers)):   
			if numbers[min_idx] > numbers[j]:   # check if a smaller number was found
				min_idx = j   # update smaller number index

		if min_idx != i:   # check if a smaller number was found, if yes, swap places
			numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

	return numbers
