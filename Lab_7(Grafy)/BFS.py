# Kolejka odsyłaczowa
class KolejkaElement:  # klasa elementu kolejki
    def __init__(self, val=0, poprzedni=None):  # konstruktor musi zawierać referencję do poprzedniego elementuw kolejce
        self.v = val
        self.nastepny = None
        if poprzedni != None:  # je?li istnieje poprzedni:
            poprzedni.nastepny = self  # ustawia, że następujący po nim jest

class Kolejka:  # klasa Kolejki
    def __init__(self):
        self.poczatek = None  # ustawia że nie ma elementu na początku, ani na końcu
        self.koniec = None

    def dodaj(self, val):  # metoda dodaje do kolejki
        el = KolejkaElement(val, self.koniec)  # tworzy element
        self.koniec = el  # ustawia go na koniec
        if self.poczatek == None:  # i jeżli początek jest pusty
            self.poczatek = self.koniec  # ustawia go na koniec

    def usun(self):  # usuwa element z początku
        if self.poczatek != None:  # żeby nie odwoływać się do None
            self.poczatek = self.poczatek.nastepny

        if self.poczatek == None:  # jeżli okazało się, że już nie ma elementów
            self.koniec = None  # usuwa element z końca kolejki

    def pobierz(self):  # zwraca pierwszy element z kolejki
        if self.poczatek != None:
            return self.poczatek.v

        return None

    def jestPusta(self):  # sprawdza, czy jest pusta
        if self.poczatek != None:
            return False

        return True

# zbiór sąsiadujących wierzchołków do wierzchołka nr v
def N(v, G):
    S = [-99]
    for i in range(len(G)):
        if G[v][i] == 1:
            if S[0] != -99:
                S.append(i)
            else:
                S[0] = i
    print(S)
    return S

class Graf:  # klasa Graf
    parent = 0
    d = 0
    visited = False

def BFS(G, s, Data):
    Q = Kolejka()
    size = len(G)
    for v in range(size):
        Data[v].visited = False

    Data[s].d = 0
    Data[s].visited = True
    Data[s].parent = None
    Q.dodaj(s)

    while Q.jestPusta() == False:
        u = Q.pobierz()
        Q.usun()
        for i in range(size):
            for v in N(i, G):
                if v >= 0 and Data[v].visited == False:
                    print("IN")
                    Data[v].visited = True
                    Data[v].d = Data[u].d + 1
                    Data[v].parent = u
                    Q.dodaj(v)
            for i in range(size):
                print(Data[i].d)
                print(Data[i].visited)
                print(Data[i].parent)
                print()


s = 0                   # numer wierzchołka startowego, numeracja 0, 1, .. ,n
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
Data = []

for i in range(len(G)):
    Data.append(Graf())

BFS(G, s, Data)