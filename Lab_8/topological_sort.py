# Sortowanie topologiczne układa wierzchołki w pewnym porządku (z wierzchołka po wewj idą krawędzie na prawo)
# zastosowanie:
#      wierzchołki - zadania do wykonania
#      krawędzie układają zadania w porządku chronologicznym (mówią które zadanie ma być wykonane innym)

class Metadata:
    def __init__(self):
        self.parent = None
        self.d = 0
        self.visited = False
        self.entry = 0
        self.process = 0

#def printPath(i, metadata):
#    id = i
#    print(f'{i}', end="")
#    while i != None and metadata[i].parent != None:
#        print(f' <- {metadata[i].parent}', end="")
#        i = metadata[i].parent
#    print(f'\tt:{metadata[id].entry}/{metadata[id].process}')

time = 0
topologicalSorted = []
def DFS(G):
    global time
    V = len(G)      # liczba wierzchołków
    metadata = [None] * V
    for i in range(V):
        metadata[i] = Metadata()

    def DFSVisit(u):
        global time
        time +=1
        metadata[u].visited = True
        metadata[u].entry = time

        # tworzymy listę sąsiadów wierzchołka "u"
        neighbours = []
        for j in range(len(G[u])):
            vertex = G[u][j]
            neighbours.append(vertex)

        for v in neighbours:
            if not metadata[v].visited:
                metadata[v].parent = u
                DFSVisit(v)
        time +=1
        metadata[u].process = time
        topologicalSorted.append(u)

    for v in range(V):      # in liczba wierzchołków
        metadata[v].visited = False
        metadata[v].parremt = None

    for v in range(V):      # in liczba wierzchołków
        if not metadata[v].visited:
            DFSVisit(v)

    #for i in range(V):
    #    printPath(i, metadata)

    topologicalSorted.reverse()
    print(topologicalSorted)


G = [[1, 2],
    [3, 4],
    [5, 6],
    [],
    [6],
    [],
    [3]]

DFS(G)
