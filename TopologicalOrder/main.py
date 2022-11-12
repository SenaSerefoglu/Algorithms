from digraph_matrix_api import *
    
def topological_order():
    for i in range(g.v()):
        if control[i]==0:
            control[i]=1
            travel(i)
    
def travel(D):
    for i in range(g.v()):
        if g.adj[D][i]==1 and control[i]==0:
            control[i]=1
            travel(i)
    order.append(D)



if __name__ == "__main__":
    g= Digraph(6)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(1,4)
    g.addEdge(1,5)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(2,5)
    
    print (g)

    control= [0]*g.v()
    order = []
    g=g.reverse()
    topological_order()
    print(order)