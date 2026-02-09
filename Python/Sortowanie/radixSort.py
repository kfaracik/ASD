def countingSort(A, P, k, i):
    B = [0]*len(A)
    C = [0]*k

    for i in P:             C[i] +=1        #=  for i in range(len(A)): C[A[i]] +=1,   zlicza ile  występuje elementów o danej wartości (indeks w tab C)
    for i in range(1, k):   C[i]+=C[i-1]    # sumuje: aktualna wart + poprzednia
    for i in range(len(A)-1, -1, -1):       # liczymy ile jest mniejszych elementów od danego
        C[P[i]] -=1
        B[C[P[i]]] = A[i]

    for i in range(len(A)): A[i] = B[i]

def printTab(t):
    print("| ", end='')
    for i in range(len(t)):
        print(f'{t[i]} | ', end='')
    print()

def radixSort(A):      # czasami lepszy niż countSort
    i=0
    P=[0]*len(A)

    while A[0] > 10**i:
        position(A, P, i)
        countingSort(A, P, 10, i)   # i - aktualnie sortowana pozycja, k=10 - klucze, cyfruy 0, 1, ..., 9
        i+=1
        print(f'Numbers {i} position:')
        printTab(P)
        print(f'Sorted array by {i} position:')
        printTab(A)
        print()

def position(A, P, i):
    for j in range(0, len(A)):
        P[j] = (A[j]//(10**i))%10

t = [ 2000, 1999, 1357, 756]
printTab(t)

radixSort(t)
