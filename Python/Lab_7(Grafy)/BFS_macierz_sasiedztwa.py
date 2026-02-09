# BFS  - Znajduje najkrótsze ścieżki w grafie do każdego wierzchoła
# reprezentacja macierzowa O(n^2)   [lisy sąsiedzwa lepsza O(V+E)]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.elements = 0

    def enqueue(self, value):
        node = Node(value)

        if self.back == None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        value = self.front.value
        self.front = self.front.next
        if self.front == None:
            self.back = None

        return value

    def is_empty(self):
        return self.front == None


class Metadata:
    def __init__(self):
        self.parent = None
        self.dist = 0
        self.visited = False


def BFS(G, s):
    # G to macierz opisująca graf: G[i][j]==1 jeśli jest
    # wierzchołek z i do j. W przeciwnym razie G[i][j]=0
    # s to numer wierzchołka źródłowego

    N = len(G)
    metadata = [None] * N
    for i in range(N):
        metadata[i] = Metadata()

    queue = Queue()

    metadata[s].visited = True
    queue.enqueue(s)

    while not queue.is_empty():
        # bierzemy pierwszy wierzchołek z kolejki
        vertexIdx = queue.dequeue()

        neighbours = []
        for i in range(N):
            if G[vertexIdx][i] == 1:
                neighbours.append(i)

        # liczymy odległość wszystkich sąsiadów danego wierzchołka
        for i in neighbours:
            if not metadata[i].visited:
                metadata[i].visited = True
                metadata[i].dist = metadata[vertexIdx].dist + 1
                metadata[i].parent = vertexIdx

                queue.enqueue(i)
                
    # (wierzchołek końcowy, odległość od źródła)
    result = []   
    for meta in metadata:
        result.append((i, meta.dist))
    
    # wypisuje najkrótsze ścieżki do wszystkich wierzchołków
    for i in range(N):
        printPath(i, metadata, s)

    return result

def printPath(i, metadata, s):
    distnace = metadata[i].dist
    print(f'{i} <- ', end = "")
    while i != None and metadata[i].parent != s:
        print(f'{metadata[i].parent} <- ', end = "")
        i = metadata[i].parent
    print(f'{s}\t d: {distnace}')


G = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0]]

BFS(G, 0)
