from InsertionSort import insertion_sort
from SelectionSort import selection_sort
from MergeSort import merge_sort
from HeapSort import heap_sort
import time


def process_inputfile():
	filename = input("Type the input filename (example: 'num.1000.1.in'): ")

	path = "inputs/" + filename
	unsorted_list = []
	input_file = open(path, "r")

	for number in input_file:
		number = number[:-1]   # remove \n
		unsorted_list.append(int(number))   # parse number from str to int and add in a list

	return unsorted_list, filename


def generate_outputfile(numbers, algorithm_name, filename):
	path = "outputs/" + algorithm_name + "/" + filename + "out"
	output_file = open(path, "w")

	for num in numbers:
		output_file.write(str(num))   # parse number from int to str and write in a file
		output_file.write("\n")

	print("> Output file " + filename.split("in")[0] + "out created in outputs dir.")


if __name__ == '__main__':

	while True:
		print("\n\n      S O R T I N G    A L G O R I T H M S\n")
		print(">> Type a number to select the sorting algorithm or to exit the program: \n")
		print("[1] - Insertion Sort")
		print("[2] - Selection Sort")
		print("[3] - Merge Sort")
		print("[4] - Quick Sort")
		print("[5] - Heap Sort")
		print("[6] - Exit")
		option = input("Option: ")

		if option == '1':   # Insertion Sort
			numbers, filename = process_inputfile()

			print("\nInsertion Sort running...")
			start_time = time.time()   # get initial time
			numbers = insertion_sort(numbers)
			print("\n> Insertion Sort finished with sorting time: %s seconds." % "{0:.3f}".format(time.time() - start_time))

			generate_outputfile(numbers, "insertion_sort", filename.split("in")[0])
			print("---------------------------------------------------------------")

			time.sleep(2)

		elif option == '2':   # Selection Sort
			numbers, filename = process_inputfile()

			print("\nSelection Sort running...")
			start_time = time.time()   # get initial time
			numbers = selection_sort(numbers)
			print("\n> Selection Sort finished with sorting time: %s seconds." % "{0:.3f}".format(time.time() - start_time))

			generate_outputfile(numbers, "selection_sort", filename.split("in")[0])
			print("---------------------------------------------------------------")

			time.sleep(2)

		elif option == '3':   # Merge Sort
			numbers, filename = process_inputfile()

			print("\nMerge Sort running...")
			start_time = time.time()   # get initial time
			merge_sort(numbers)
			print("\n> Merge Sort finished with sorting time: %s seconds." % "{0:.3f}".format(time.time() - start_time))

			generate_outputfile(numbers, "merge_sort", filename.split("in")[0])
			print("---------------------------------------------------------------")

			time.sleep(2)

		elif option == '4':   # Quick Sort
			numbers, filename = process_inputfile()

			print("\nQuick Sort running...")
			start_time = time.time()   # get initial time
			merge_sort(numbers)
			print("\n> Quick Sort finished with sorting time: %s seconds." % "{0:.3f}".format(time.time() - start_time))

			generate_outputfile(numbers, "quick_sort", filename.split("in")[0])
			print("---------------------------------------------------------------")

			time.sleep(2)

		elif option == '5':   # Heap Sort
			numbers, filename = process_inputfile()

			print("\nHeap Sort running...")
			start_time = time.time()   # get initial time
			merge_sort(numbers)
			print("\n> Heap Sort finished with sorting time: %s seconds." % "{0:.3f}".format(time.time() - start_time))

			generate_outputfile(numbers, "heap_sort", filename.split("in")[0])
			print("---------------------------------------------------------------")

			time.sleep(2)

		elif option =='6':   # Exit
			print("\nExiting...")
			break
	