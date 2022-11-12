class BreadthFirstPaths:
	def __init__(self, G, s):
		self.marked = []
		self.edgeTo = []

		self.s = s
		for i in range(G.v()):
			self.marked.append(False)
			self.edgeTo.append(-1)
		self.bfs(G, s)

	def bfs(self, G, s):
		queue = []
		self.marked[s] = True
		queue.insert(0, s)
		while len(queue) != 0:
			v = queue.pop(-1)
			w = G.adj[v]
			while w != None:
				if not self.marked[w.key]:
					self.edgeTo[w.key] = v
					self.marked[w.key] = True
					queue.insert(0, w.key)
				w = w.next

	def hasPathTo(self, v):
		return self.marked[v]

	def pathTo(self, v):
		if not self.hasPathTo(v):
			return None
	
		x = v
		l = []
		while x != self.s:
			l.insert(0, x)
			x= self.edgeTo[x]
		l.insert(0, self.s)
	
		return l