import time

def insertion_sort(numbers):
	start_time = time.time()   # get initial time

	for j in range(1,len(numbers)):   # loop through numbers list starting from the second number (index 1)
		pivot = numbers[j]
		i = j-1   # get previous index
        
		while (i > -1) and (pivot < numbers[i]):   # compare numbers and search for the index that will receive the pivot
		    numbers[i+1] = numbers[i]   #  bigger number in bigger index
		    i = i-1   # move one index more on the direction of array beginning 

		numbers[i+1] = pivot   # numbers[i] < pivot, so, place pivot in the right position

	sorting_time = time.time() - start_time   # calculate sorting time: final - initial
	print("\n> Insertion Sort finished with sorting time: %s seconds." % "{0:.3f}".format(sorting_time))
	return numbers