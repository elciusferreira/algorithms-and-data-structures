def insertion_sort(numbers):
	# loop through numbers list starting from the second number (index 1)
	for j in range(1,len(numbers)):   
		pivot = numbers[j]
		i = j-1   # get previous index
        
        # compare numbers and search for the index that will receive the pivot
		while i > -1 and pivot < numbers[i]:   
		    numbers[i+1] = numbers[i]   #  bigger number in bigger index
		    i = i-1   # move one index more on the direction of array beginning 

		numbers[i+1] = pivot   # numbers[i] < pivot, so, place pivot in the right position

	return numbers