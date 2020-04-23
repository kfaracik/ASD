# Algorytm wydajny np do posortowania 1.000.000.000 osób względem dnia trygodnia w którym się urodzili (klucze 7 dni)

def countingSort(A, k):
    B = [0]*len(A)
    C = [0]*k

    printTab(A)
    printTab(B)
    printTab(C)
    
    # liczymy ile razy każdy nel z tab A występuje
    for i in A:             C[i] +=1          #=  for i in range(len(A)): C[A[i]] +=1
    for i in range(1, k):   C[i]+=C[i-1]    # liczymy ile jest elementów <=  od danego
    for i in range(len(A)-1, -1, -1):       # sortujemy
        C[A[i]] -=1
        B[C[A[i]]] = A[i]

    for i in range(len(A)): A[i] = B[i]

    printTab(A)

def printTab(t):
    print("| ", end='')
    for i in range(len(t)):
        print(f'{t[i]} | ', end='')
    print()

t = [1, 4, 3, 6, 5, 2]
printTab(t)

countingSort(t, 6+1)        # k+1 = range of index in array 0,... k, k+1
printTab(t)
