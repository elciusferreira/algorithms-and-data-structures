import time

def selection_sort(numbers):
	start_time = time.time()   # get initial time

	for i in range(len(numbers)):   # loop through numbers list
		min_idx = i   # set first number as smaller

		for j in range(i+1, len(numbers)):   # loop through numbers list starting from the subsequent number
			if numbers[min_idx] > numbers[j]:   # check if a smaller number was found
				min_idx = j   # update smaller number index

		if min_idx != i:   # check if a smaller number was found, if yes, swap places
			aux = numbers[i]   
			numbers[i] = numbers[min_idx]
			numbers[min_idx] = aux

	sorting_time = time.time() - start_time    # calculate sorting time: final - initial
	print("\n> Selection Sort finished with sorting time: %s seconds." % "{0:.3f}".format(sorting_time))
	return numbers
