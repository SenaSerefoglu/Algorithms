class Digraph(object):
    
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = []
        for i in range (self.V):
            ll = []
            for j in range (self.V):
                ll.append(0)
            self.adj.append(ll)         # self.adj = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    # Returns the number of vertices in the digraph.
    def v(self):
        return self.V

    # Returns the number of edges in the digraph.
    def e(self):
        return self.E
    
    # Adds the directed edge v->w to the digraph.
    def addEdge(self, v, w):
        self.adj[v][w] = 1
        self.E = self.E + 1

    # Returns the reverse of the digraph.
    def reverse(self):
        R = Digraph(self.V)
        for v in range(self.V):
            for w in range (self.V):
                if self.adj[v][w] == 1:
                    R.addEdge(w, v)
        return R

    def __str__(self):
        s = str(self.V) + " Vertices, " + str(self.E) + " Edges\n"
        for v in range(self.V):
            s = s + str(v) + ": "
            W = self.adj[v]
            for w in W:
                s = s + str(w) + " "
            s = s + "\n"
        return s


"""if __name__ == "__main__":
     mygraph = Digraph(5)
     print (mygraph)
     mygraph.addEdge(0, 1)
     print (mygraph)
     mygraph.addEdge(0, 2)
     mygraph.addEdge(0, 3)
     mygraph.addEdge(1, 3)
     mygraph.addEdge(2, 3)
     mygraph.addEdge(3, 4)

     print (mygraph)
     print()
     reversed = mygraph.reverse()
     print (reversed)
     print()"""        