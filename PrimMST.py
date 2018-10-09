import sys 

class PrimGraph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	# a support function to print the constructed MST 
	def printMST(self, parent): 
		print ("\n> Following are the edges in the constructed MST")
		sum = 0
		for i in range(1,self.V): 
			print(parent[i],"-",i,"  ",self.graph[i][parent[i]])
			sum += self.graph[i][parent[i]]
		print("\n> Result:", sum)

	# a support function to find the vertex with 
	# minimum distance value
	def minKey(self, key, mstSet): 
		min = sys.maxsize # initilaize min value 

		for v in range(self.V): 
			if key[v] < min and mstSet[v] == False: 
				min = key[v] 
				min_index = v 

		return min_index 

	def primMST(self): 
		key = [sys.maxsize] * self.V # initiate keys with large value
		parent = [None] * self.V # store constructed MST 
		key[0] = 0 # make key 0 so that this vertex is picked as first vertex 
		mstSet = [False] * self.V # control vertices processed and not processed yet
		parent[0] = -1 # First node is always the root 

		for cout in range(self.V): 
			# pick the minimum distance vertex from the set of vertices not yet processed
			u = self.minKey(key, mstSet) 
			mstSet[u] = True # Put the minimum distance vertex inside

			# update dist value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shortest path tree 
			for v in range(self.V): 
				# update the key only if graph[u][v] is smaller than key[v] 
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
						key[v] = self.graph[u][v] 
						parent[v] = u 

		self.printMST(parent) 
		
