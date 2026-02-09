class Graf:  # klasa Graf
    parent = None
    d = 0
    visited = False

def N(v, G):               # zbiór sąsiadujących wierzchołków do wierzchołka nr v
    S = [-99]
    for i in range(len(G)):
        if G[v][i] == 1:
            if S[0] != -99:
                S.append(i)
            else:
                S[0] = i
    #print(S)
    if S[0] == -99:         # pusty wiersz
        S = []

    return S


s = 1                   # numer wierzchołka startowego

G = [[0,1,1,0],
     [0,0,0,1],
     [0,1,0,1],
     [0,0,0,0]]

for i in range(len(G)):
    for v in N(i, G):
        print(f'{i} {v}')

Data = []
for i in range(len(G)):
    Data.append(Graf())

#print(Data[0].d)
