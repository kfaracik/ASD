class Graf:         # struktura Graf, przechowuje d - odległość od początkowego wierzchołka oraz wybranego rodzica w danej ścieżce
    parent = None
    d = 999999      # symbolizuje inf

def printData(Data, G):
    for i in range(len(G)):
        for j in range(len(G[i])):
            print(f'v: {i} -> {G[i][j][0]}\tcost: {G[i][j][1]}\t\td: {Data[i].d}\tparent: {Data[i].parent} ')

def size_E(G):      # ilość krawędzi
    size = 0
    for i in range(len(G)):
        size += len(G[i])
    print(size)
    return size

G = [[(1, 10), (2, 3)],
    [(2, 4), (3, 2)],
    [(1, 4), (3, 8)],
    [(4, 9)],
    [(3, 9)]]
# ilość wierzchołkó = len(G)

Data = []
for i in range(size_E(G)):
    Data.append(Graf())

printData(Data, G)