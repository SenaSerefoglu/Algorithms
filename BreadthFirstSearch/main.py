from bfp import BreadthFirstPaths
from graph import Graph



list0=[]
def filetolist():
    #appends all the words to a list from txt file
    file = open("words.txt", "r")
    for line in file:
        line=line.strip("\n")[0:5]
        list0.append(line)
filetolist()

def get_index(s):
    # Pulls the word that is indexed in the list.
    i=0
    for item in list0:
        if item == s:
            return i
        i+=1

def add_to_graph(graph):
    # Creates a graph by adding edges between words that are one character apart.
    for i in range(len(list0)):
        for j in range(i,len(list0)):
            diff=0
            for a, b in zip(list0[i], list0[j]):
                if a != b:
                    diff+=1
            if diff==1:
                graph.addEdge(i,j)

def get_path(graph):
    # Takes the graph and returns the shortest path between two words.
    string1 =input("Please enter a valid word: ")
    string2 =input("Please enter a valid word: ")
    i1=get_index(string1)
    i2=get_index(string2)
    path =BreadthFirstPaths(graph,i1).pathTo(i2)
    i=0
    if path == None:
        return "There is no path between these two words."
    for index in path:
        path[i]=list0[index]
        i+=1
    return path


mygraph= Graph(len(list0))
add_to_graph(mygraph)
print(get_path(mygraph))