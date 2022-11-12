class EdgeWeightedGraph :
    class Node:
        def __init__(self, key, weight, next):
            self.key = key
            self.next = next
            self.weight = weight

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = []
        for i in range(V):
            self.adj.append(None)

    def v(self):
        return self.V

    def e(self):
        return self.E

    def addEdge(self, v1, v2, weight):
        self.adj[v1] = EdgeWeightedGraph.Node(v2, weight, self.adj[v1])
        self.adj[v2] = EdgeWeightedGraph.Node(v1, weight, self.adj[v2])
        self.E = self.E + 1

    def adjj(self, v):
        vv = self.adj[v]
        t = []
        while vv != None:
            # Edges are shown as tuple (v, w, weight).
            t.append((v, vv.key, vv.weight))
            vv = vv.next
        return t

    def edges(self):
        list =  []
        for v in range (self.V):
            selfLoops = 0
            adj_edges = self.adjj(v)
            for adj_edge in adj_edges:
                # We check w > v for appending edges for once.
                if adj_edge[1] > v:
                    list.append(adj_edge)
                # There coulde be a looped edges in the graph (w = v),
                # we must add thoose type of edges once aswell.
                elif (adj_edge[1] == v):
                    if (selfLoops % 2 == 0) :
                        list.append(adj_edge)
                    selfLoops += 1
        return list

    def __str__(self):
        s = str(self.V) + " Vertices, " + str(self.E) + " Edges\n"
        for v in range(self.V):
            s = s + str(v) + ": "
            w = self.adj[v]
            while w != None:
                s = s + str(w.key) + " "
                w = w.next
            s = s + "\n"
        return s

# Test Function
"""if __name__ == "__main__":
    mygraph = EdgeWeightedGraph(5)
    mygraph.addEdge(0, 1, 10)
    mygraph.addEdge(0, 2, 8)
    mygraph.addEdge(0, 3, 6)
    mygraph.addEdge(1, 3, 12)
    mygraph.addEdge(2, 3, 4)
    mygraph.addEdge(3, 4, 1)
    mygraph.addEdge(1, 1, 3)

    print (mygraph.adjj(0))
    print (mygraph)
    print ("---------------")
    print (mygraph.edges())"""