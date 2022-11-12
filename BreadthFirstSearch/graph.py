class Graph:
    class Node:
        def __init__(self, key, next):
            self.key = key
            self.next = next

    def __init__(self, V):
        self.V = V  # V dor Vertex count
        self.E = 0  # E for Edge count
        self.adj = []
        for i in range(V):
            self.adj.append(None)

    def v(self):
        return self.V

    def e(self):
        return self.E

    def addEdge(self, v, w):
        self.adj[v] = Graph.Node(w, self.adj[v])
        self.adj[w] = Graph.Node(v, self.adj[w])
        self.E = self.E + 1