from InsertionSort import insertion_sort
from SelectionSort import selection_sort
from MergeSort import merge_sort
from HeapSort import heap_sort
from KruskalMST import KruskalGraph
from PrimMST import PrimGraph
from DijkstraMST import DijkstraGraph
from Knapsack import knapsack
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


def process_MST_inputfile():
	filename = input("Type the input filename (example: 'kru_pri_dij10.txt'): ")

	path = "inputs/" + filename
	input_file = open(path, "r")

	i = 0
	first_line = True
	adj_matrix = []

	for line in input_file:
		if first_line == True:
			vertices = int(line[:-1])
			adj_matrix = [0] * vertices

			for j in range(vertices):
				adj_matrix[j] = [0] * vertices

			first_line = False

		else:
			line = line[:-1].split(' ')

			if line[-1] == '':
				line = line[:-1]

			for number in range(len(line)):
				adj_matrix[i][number+i+1] = int(line[number])
				adj_matrix[number+i+1][i] = int(line[number])
			i += 1

	return vertices, adj_matrix

def process_knapsack_input():
	filename = input("Type the knapsack input filename (example: 'knapsack01.txt'): ")

	path = "inputs/" + filename
	input_file = open(path, "r")

	first_line = True
	values = []
	weights = []
	for line in input_file:
		if first_line == True:
			n, W = line[:-1].split(' ')   # get items quantity and knapsack weigth
			first_line = False

		else:
			w, v = line[:-1].split(' ')   # get item weigth and value
			values.append(int(v))
			weights.append(int(w))

	return int(n), int(W), values, weights


def generate_outputfile(numbers, algorithm_name, filename):
	path = "outputs/" + algorithm_name + "/" + filename + "out"
	output_file = open(path, "w")

	for num in numbers:
		output_file.write(str(num))   # parse number from int to str and write in a file
		output_file.write("\n")

	print("> Output file " + filename.split("in")[0] + "out created in outputs dir.")


if __name__ == '__main__':

	while True:
		print("\n\n      A L G O R I T H M S\n")
		print(">> Type a number to select an algorithm or to exit the program: \n")
		print("[1] - Insertion Sort")
		print("[2] - Selection Sort")
		print("[3] - Merge Sort")
		print("[4] - Quick Sort")
		print("[5] - Heap Sort")
		print("[6] - KruskalMST")
		print("[7] - PrimMST")
		print("[8] - DijkstraMST")
		print("[9] - 0/1 Greedy Knapsack Problem")
		print("[10]- Exit")
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

		elif option == '6':   # Kruskal MST
			vertices, adj_matrix = process_MST_inputfile()
			g = KruskalGraph(vertices) 

			for row in range(len(adj_matrix)):
				for number in range(len(adj_matrix[row])):
					if adj_matrix[row][number] != 0:
						g.addEdge(row, number, adj_matrix[row][number])

			g.kruskalMST() 

		elif option == '7':   # Prim MST
			vertices, adj_matrix = process_MST_inputfile()
			g = PrimGraph(vertices) 

			g.graph = adj_matrix

			g.primMST() 

			time.sleep(2)

		elif option == '8':   # Dijkstra MST
			vertices, adj_matrix = process_MST_inputfile()
			g = DijkstraGraph(vertices) 

			g.graph = adj_matrix

			g.dijkstraMST(0)

			time.sleep(2) 

		elif option =='9':   # Greedy 0/1 Knapsack
			n, W, val, wt = process_knapsack_input()

			start_time = time.time()   # get initial time

			knapsack(n, W, val, wt)	

			print("\n> Greedy 0/1 Knapsack algorithm finished in: %s seconds." % "{0:.3f}".format(time.time() - start_time))

			time.sleep(2)

		elif option =='10':   # Exit
			print("\nExiting...")
			break
	