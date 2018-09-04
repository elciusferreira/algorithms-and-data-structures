def partition(numbers, first, last):
	pivot_value = numbers[first]   # pivot as the first element

	# position markers
	leftmark = first + 1
	rightmark = last

	done = False
	# loop to move the elements smaller than pivot value to its left and bigger to its right
	while not done:
		# search smaller values than pivot value by moving the position marker
		while leftmark <= rightmark and numbers[leftmark] <= pivot_value:
			leftmark += 1

		#search bigger values than pivot value by moving the position marker
		while leftmark <= rightmark and numbers[rightmark] >= pivot_value:
			rightmark -= 1

		if leftmark > rightmark:   # check if the markers crossed
			done = True   # finish loop

		else:   # swap the markers values
			numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]

	numbers[first], numbers[rightmark] = numbers[rightmark], numbers[first]   # swap places between pivot and rightmarker
	return rightmark   # return pivot index


def quick_sort(numbers, first, last):
	if first < last:
		splitpoint = partition(numbers, first, last) 

		# recursion
		quick_sort(numbers, first, splitpoint - 1)
		quick_sort(numbers, splitpoint + 1, last)