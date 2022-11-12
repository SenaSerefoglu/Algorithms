from QuickFindUF import QuickFindUF
from weighted_graph import EdgeWeightedGraph

class TersKruskalMST:
    def __init__(self, EWG):
        # mst doesnt have any edge for the first time.
        controlList=[]
        for i in range(EWG.v()):
                controlList.append(None)
        self.mst = [] # mst = [(v1, v2, weight), (v1, v2, weight), (), (), ....]
        self.weight = 0

        # We create a list of edges in the graph and sort them according to the edge weights.
        pq = sorted(EWG.edges(), key=lambda x: x[2])

        # The main loop of Kruskal Algorithm
        while len(self.mst)< EWG.v()-1:
            connected=True
            # Mark all nodes as False
            for i in range(EWG.v()):
                controlList[i]=False
            # pop the edge with the highest weight from pq.
            e = pq.pop(-1)
            uf = QuickFindUF(EWG.v())
            # Mark the nodes that are elements of the pq list as True and connect them with uf.union.
            for item in pq:
                if not uf.isConnected(item[0],item[1]):
                    uf.union(item[0],item[1])
                controlList[item[0]]=True
                controlList[item[1]]=True
            # Check if all nodes in EWG are connected.
            for i in range(EWG.v()):
                if not uf.isConnected(i,i-1):
                    connected=False
            # Add the edge to the mst if all nodes in EWG are connected or all nodes are not marked as True.
            if False in controlList or connected==False:
                pq.insert(0,e)
                self.mst.append(e)
                self.weight+=e[2]

    def edges(self):
        return self.mst

    def weight(self):
        return self.weight


mygraph = EdgeWeightedGraph(8)
mygraph.addEdge(0, 1, 6)
mygraph.addEdge(0, 5, 12)
mygraph.addEdge(1, 2, 14)
mygraph.addEdge(1, 3, 8)
mygraph.addEdge(1, 5, 5)
mygraph.addEdge(2, 3, 3)
mygraph.addEdge(3, 4, 10)
mygraph.addEdge(4, 5, 7)
mygraph.addEdge(4, 7, 15)
mygraph.addEdge(5, 6, 9)

mymst = TersKruskalMST(mygraph)
print (mymst.edges())
print (mymst.weight)
