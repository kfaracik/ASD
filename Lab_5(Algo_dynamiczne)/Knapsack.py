def knapsack(W, P, MaxW, M):
    n = len(W)
    F = [None]*n
    for i in range(n):
        F[i] = [0]*(MaxW + 1)   #Tworzymy tab dwuwymiarową

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]
    M[0][W[0]] = 1              # set 1 row in mapa

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])

            if F[i][w-1] != F[i][w]:
                M[i][w] = 1     # set mapa

    printTab(F, n-1, MaxW)
    printTab(M, n-1, MaxW)
    return F[n-1][MaxW]

def printTab(tab, w, k):
    for i in range(0, w):
        print(f'{tab[i]}')
    print()

# tab z indeksami wziętych elementów

MaxW = 10
W = [4, 1, 2, 4, 3, 5, 10, 3]
P = [7, 3, 2, 10, 4, 1, 7, 2]

M = [None]*len(W)
for i in range(len(W)):
    M[i] = [0] * (MaxW + 1)  # Tworzymy tab dwuwymiarową

knapsack(W, P, MaxW, M)
