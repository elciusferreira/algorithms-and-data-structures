def heapfy(numbers, size, parent):
	largest = parent   # set parent as largest number
	left_child = 2 * parent + 1   # find left child index by parent index
	right_child = 2 * parent + 2   # find right child index by parent index

	# check if left child is larger then parent
	if left_child < size and numbers[largest] < numbers[left_child]:
		largest = left_child

	# check if right child is larger then parent or left child
	if right_child < size and numbers[largest] < numbers[right_child]:
		largest = right_child

	# swap parent and child if needed
	if largest != parent:
		numbers[parent], numbers[largest] = numbers[largest], numbers[parent]   # swap
		heapfy(numbers, size, largest)   # heapfy child subtree


def heap_sort(numbers):
	size = len(numbers)

	# build a maxheap
	for i in range(size, -1, -1):
		heapfy(numbers, size, i)

	# extract elements one by one
	for i in range(size-1, 0, -1):
		numbers[i], numbers[0] = numbers[0], numbers[i]   # swap
		heapfy(numbers, i, 0)