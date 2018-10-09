def process_MST_inputfile():
	#filename = input("Type the input filename (example: 'kru_pri_dij10.txt'): ")

	path = "inputs/kru_pri_dij10.txt"
	unsorted_list = []
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
			print(line)

			for number in range(len(line)):
				adj_matrix[i][number+i+1] = int(line[number])
				adj_matrix[number+i+1][i] = int(line[number])
			i += 1

	return vertices, adj_matrix

vertices, adj_matrix = process_MST_inputfile()

print(vertices)
for row in range(len(adj_matrix)):
	print(adj_matrix[row])

for row in range(len(adj_matrix)):
	print(adj_matrix[row])
	for number in range(len(adj_matrix[row])):
		if adj_matrix[row][number] != 0:
			print(adj_matrix[row][number], row, number)
	print()

print(adj_matrix)