# Algorytm przeszukuje graf, szukając najgłębszych możliwych ścieżek
# Złożoność zależy od reprezentacji grafu, najlepsza dla listy sąsiedztwa O(V+E), gdzie V to zb. wierzchołków a E to zb ktawędzi
# Listy sąsiedztwa O(V+E)
# Macierz sąsiedztwa O(V^2)

class Metadata:
    def __init__(self):
        self.parent = None
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

def DFS(G):
    V = len(G)      # liczba wierzchołkó
    metadata = [None] * V
    for i in range(V):
        metadata[i] = Metadata()

    def DFSVisit(u, time):
        time +=1
        metadata[u].visited = True
        metadata[u].entry = time

        # tworzymy listę sąsiadów wierzchołka "u"
        neighbours = []
        for i in range(V):
            if G[u][i] == 1:
                neighbours.append(i)

        for v in neighbours:
            if not metadata[v].visited:
                metadata[v].parent = u
                time = DFSVisit(v, time)
        time +=1
        metadata[u].process = time
        return time

    time = 0
    for v in range(V):      # in liczba wierzchołków
        metadata[v].visited = False
        metadata[v].parremt = None

    for v in range(V):      # in liczba wierzchołków
        if not metadata[v].visited:
            time = DFSVisit(v, time)

    for i in range(V):
        printPath(i, metadata)

G = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0]]

DFS(G)
