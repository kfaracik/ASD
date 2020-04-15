def LIS_slow(A):                         # złożoność O(n^2)
    n = len(A)
    F = [1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j]+1:
                F[i] = F[j]+1
    return max(F)

#def LIS(A):                            # O( n*log(n) )
    #vector<int> Warstwa[n];
    #int Ostatni = 0, index;
    #for (int i=0; i<n; i += 1)
    #    wczytaj(A);
    #    index = lower_bound(Warstwa.back, A);
    #    //Czyli najmniejszy element większy od A (lub równy!).

    #    Warstwa[index].Push_Back(A);
    #    Ostatni = max(Ostatni, index); 
    #//tutaj bierzemy maksimum ze wszystkich numerów
    #//niepustych warstw
    #wypisz(Ostatni);


A = [1, 3, 2, 5, 4, 10]

print(LIS_slow(A))
