def LIS(A):
    n = len(A)
    F = [1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j]+1:
                F[i] = F[j]+1
    return max(F)

A = [1, 3, 2, 5, 4, 10]

print(LIS(A))