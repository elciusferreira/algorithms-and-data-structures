from InsertionSort import insertion_sort
from SelectionSort import selection_sort
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


def generate_outputfile(numbers, filename):
	path = "outputs/insertion_sort/" + filename + "out"
	output_file = open(path, "w")

	for num in numbers:
		output_file.write(str(num))   # parse number from int to str and write in a file
		output_file.write("\n")

	print("> Output file " + filename.split("in")[0] + "out created in outputs dir.")


if __name__ == '__main__':

	while True:
		print("\n\n      S O R T I N G    A L G O R I T H M S\n")
		print(">> Type 1 or 2 to select the sorting algorithm and 3 to exit the program: \n")
		print("[1] - Insertion Sort")
		print("[2] - Selection Sort")
		print("[3] - Exit")
		option = input("Option: ")

		if option == '1':
			unsorted_list, filename = process_inputfile()
			print("\nInsertion Sort running...")
			sorted_list = insertion_sort(unsorted_list)
			generate_outputfile(sorted_list, filename.split("in")[0])
			print("---------------------------------------------------------------")
			time.sleep(2)

		elif option == '2':
			unsorted_list, filename = process_inputfile()
			print("\nSelection Sort running...")
			sorted_list = selection_sort(unsorted_list)
			generate_outputfile(sorted_list, filename.split("in")[0])
			print("---------------------------------------------------------------")
			time.sleep(2)

		elif option =='3':
			print("\nExiting...")
			break
	