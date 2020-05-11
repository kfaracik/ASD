import queue

class Metadata:
    def __init__(self):
        self.parent = None
        self.d = 0
        self.visited = False

def printPath(i, metadata):
    distnace = metadata[i].d
    print(f'{i}', end="")
    while i != None and metadata[i].parent != None:
        print(f' <- {metadata[i].parent}', end="")
        i = metadata[i].parent
    print(f'\td: {distnace}')

def BFS(G, s):
    Q = queue.Queue()
    size = len(G)
    Data = [None] * size
    for i in range(size):
        Data[i] = Metadata()

    Data[s].d = 0
    Data[s].visited = True      # jeśli wiemy że z wierzchołka s można osiągnąć wszystkie inne
    Data[s].parent = None       # jeżeli nie wiemy to trzeba będzie startować z kilku wirzchołków ale uprzednio ustawić w wierzchołek.parent = None
    Q.put(s)

    while(not Q.empty()):
        u = Q.get()

        neighbours = []
        for j in range(len(G[u])):
            vertex = G[u][j]
            neighbours.append(vertex)

        for v in neighbours:                       # zb. wierzchołków do których są krawędzie z v (zb. sąsiadów v)
            if not Data[v].visited:
                Data[v].visited = True
                Data[v].d = Data[u].d + 1
                Data[v].parent = u
                Q.put(v)

    for i in range(size):
        printPath(i, Data)

# graf nieważony => koszt krawędzi = 1
G = [[1, 2],
    [3, 4],
    [5, 6],
    [],
    [6],
    [],
    [3]]
s = 0                   # numer wierzchołka startowego, numeracja 0, 1, .. ,n

BFS(G, s)