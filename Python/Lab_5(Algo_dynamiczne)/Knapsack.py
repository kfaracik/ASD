# 1. OPIS FUNKCJI: f(i,w) = największy zysk jaki można osiągnąć wybierająć spośród poierwszych i przedmiotów o indeksach od 0 do i, nie przekraczając zadanej wagi W
# 2. ZAPIS REKURENCYJNY:
                # Zał:
                # f(0,w) = 0    , dla w<W[0]
                #          P[0] , w > W[0]
                # f(i,0) = 0
                # w-W[i] >=0
                #   f(i,w) = max( f(i-1,w) , f(i-1,w-W[i)+P[i] )
# 3. IMPLENMEMNTACJA:

# dobra złożoność dla relatywnie małych MaxW

def knapsack(W, P, MaxW, M):
    n = len(W)
    F = [None]*n
    for i in range(n):
        F[i] = [0]*(MaxW + 1)   #Tworzymy tab dwuwymiarową

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]
    M[0][W[0]] = 1              # ustraw mape
    # ------     O(n*MaxW)   ------ złożoność do tego miejsca

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])

            if F[i][w-1] != F[i][w]:
                M[i][w] = 1     # ustaw mape
    # ------     O(n*MaxW)   ------ złożoność do tego miejsca

    printTab(F, n-1, MaxW)  # wypisuje wagi wyznaczonych przedmiotów - struktura knapsack
    printTab(M, n-1, MaxW)  # wypisuje 1 jeśli przedmiot został wzięty, 0 wpp
    printKnapsack(F, M, n-1, MaxW)

    return F[n-1][MaxW]

def printTab(tab, w, k):
    for i in range(0, w):
        print(f'{tab[i]}')
    print()

# wypisuje wagi wyznaczonych przedmiotów
def printKnapsack(F, M, w, MaxW):
    for i in range(0, w):
        for j in range(0, w):
            if M[i][j]:
                print(f'{F[i][j]}\t', end='')
            else:
                print(f'0\t', end='')
        print()

MaxW = 10
W = [4, 1, 2, 4, 3, 5, 10, 3]
P = [7, 3, 2, 10, 4, 1, 7, 2]

M = [None]*len(W)
for i in range(len(W)):
    M[i] = [0] * (MaxW + 1)

knapsack(W, P, MaxW, M)
