# Algorytm przeszukuje graf, szukając najgłębszych możliwych ścieżek
# Złożoność zależy od reprezentacji grafu, najlepsza dla listy sąsiedztwa O(V+E), gdzie V to zb. wierzchołków a E to zb ktawędzi
# Listy sąsiedztwa O(V+E)
# Macierz sąsiedztwa O(V^2)

class Metadata:
    def __init__(self):
        self.parent = None
        self.d = 0
        self.visited = False
        self.entry = 0
        self.process = 0

def printPath(i, metadata):
    id = i
    print(f'{i}', end="")
    while i != None and metadata[i].parent != None:
        print(f' <- {metadata[i].parent}', end="")
        i = metadata[i].parent
    print(f'\tt:{metadata[id].entry}/{metadata[id].process}')

time = 0
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

    for v in range(V):      # in liczba wierzchołków
        metadata[v].visited = False
        metadata[v].parremt = None

    for v in range(V):      # in liczba wierzchołków
        if not metadata[v].visited:
            DFSVisit(v)

    for i in range(V):
        printPath(i, metadata)

G = [[1, 2],
    [3, 4],
    [5, 6],
    [],
    [6],
    [],
    [3]]

DFS(G)