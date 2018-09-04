def merge_sort(numbers):
	if len(numbers) > 1:
		mid = len(numbers)//2
		# split array in two subarrays
		lefthalf = numbers[:mid] 
		righthalf = numbers[mid:]

		# recursion with each part
		merge_sort(lefthalf)
		merge_sort(righthalf)

		# merge the halves back into numbers array
		i = 0   # initial index of first subarray
		j = 0	# initial index of second subarray
		k = 0   # initial index of merged array
		# loop through both subarrays
		while i < len(lefthalf) and j < len(righthalf):   
			if lefthalf[i] < righthalf[j]:   # compare elements
				numbers[k] = lefthalf[i]   # store smaller
				i += 1

			else:
				numbers[k] = righthalf[j]
				j += 1

			k += 1

		# copy the remaining elements of lefthalf if there are any
		while i < len(lefthalf):
			numbers[k] = lefthalf[i]
			i += 1
			k += 1

		# copy the remaining elements of righthalf if there are any
		while j < len(righthalf):
			numbers[k] = righthalf[j]
			j += 1
			k += 1

