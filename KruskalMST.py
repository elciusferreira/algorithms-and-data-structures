from collections import defaultdict 

# graph class
class KruskalGraph: 

	def __init__(self,vertices): 
		self.V = vertices # number of vertices
		self.graph = [] # dict to store the graph 
		

	# add an edge to graph 
	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w]) 

	# a support function to find set of an element i
	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	# union (by rank) of two sets of x and y 
	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		# attach smaller rank tree under root of 
		# high rank tree (union by rank) 
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 

		# if ranks are the same, then make one as root 
		# and increment its rank by one 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	def kruskalMST(self): 

		result =[]   # store the resultant MST 

		i = 0   # an index variable, used for sorted edges 
		e = 0   # an index variable, used for result[] 

		# sort all the edges in non-decreasing order of their weight
		self.graph = sorted(self.graph,key=lambda item: item[2]) 

		parent = []
		rank = [] 

		# create V subsets with single elements 
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 
	
		# number of edges to be taken is equal to V-1 
		while e < self.V - 1 : 

			# pick the smallest edge and increment 
			# the index for next iteration 
			u,v,w = self.graph[i] 
			i += 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			# if including this edge does't cause cycle, 
			# include it in result and increment the index 
			# of result for next edge 
			if x != y: 
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# else discard the edge 

		# print the contents of result[] to display the built MST 
		print ("\n> Following are the edges in the constructed MST")
		sum = 0
		for u,v,weight in result:  
			print ("%d -- %d == %d" % (u,v,weight)) 
			sum += weight
		print("\n> Result:", sum)