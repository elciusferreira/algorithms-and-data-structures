import sys 

class DijkstraGraph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printSolution(self, dist): 
		print ("\n> Following are the edges in the constructed MST")
		for node in range(self.V): 
			print (node,"\t",dist[node])
			sum = dist[node]
		print("\n> Result:", sum)

	# a support function to find the vertex with 
	# minimum distance value 
	def minDistance(self, dist, sptSet): 
		min = sys.maxsize   # initilaize min value 

		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 

		return min_index 


	def dijkstraMST(self, src): 
		dist = [sys.maxsize] * self.V   # initiate dists with large value
		dist[src] = 0
		sptSet = [False] * self.V   # control vertices processed and not processed yet

		for cout in range(self.V): 
			# pick the minimum distance vertex from the set of vertices not yet processed
			u = self.minDistance(dist, sptSet) 
			sptSet[u] = True   # Put the minimum distance vertex inside

			# update dist value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shotest path tree 
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
					dist[v] = dist[u] + self.graph[u][v] 

		self.printSolution(dist)