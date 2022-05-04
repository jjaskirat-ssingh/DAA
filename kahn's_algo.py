from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list) 
		self.V = vertices 

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def topologicalSort(self):		
		in_degree = [0]*(self.V)
		
		# Traverse adjacency lists to fill indegrees of
		# vertices. This step takes O(V + E) time
		for i in self.graph:
			for j in self.graph[i]:
				in_degree[j] += 1

		queue = []
		for i in range(self.V):
			if in_degree[i] == 0:
				queue.append(i)

		cnt = 0
		top_order = []

		# One by one dequeue vertices from queue and enqueue
		# adjacents if indegree of adjacent becomes 0
		while queue:
			u = queue.pop(0)
			top_order.append(u)

			# Iterate through all neighbouring nodes
			# of dequeued node u and decrease their in-degree
			# by 1
			for i in self.graph[u]:
				in_degree[i] -= 1
				# If in-degree becomes zero, add it to queue
				if in_degree[i] == 0:
					queue.append(i)

			cnt += 1

		if cnt != self.V:
			print ("There exists a cycle in the graph")
		else :
			print (top_order)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print ("Following is a Topological Sort of the given graph")
g.topologicalSort()

