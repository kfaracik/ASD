def fib_slow(n):         # nieoptymalny O( (1+sqrt(5)/2)^n )
    if n<=1:
        return 1
    return fib_slow(n-1) + fib_slow(n-2)

def fib_DP(n):          # szybki algo dynamiczny, ale potrzeba dużo poamięci
    F = [1]*(n+1)       # tab kolejnych elementów c. fib
    for j in range(2,n+1):
        F[j] = F[j-1] + F[j-2]
    return F[n]

def fib_DP_Better(n):   # optymalne pamięciowo i obliczeniowo
    if n <= 1:  return 1
    Fj1 = 1
    Fj2 = 1
    for j in range(2, n+1):
        Fj = Fj1 + Fj2
        Fj2, Fj1 = Fj1, Fj
    return Fj


# Rekurencyja dynamiczna (zazwyczaj wolniejsza niż DP)
N = 100     # N górny zakres liczby elementów
F = [0]*N   # F[x] = 0 -> dany element ciągu nie został obliczony
F[0] = 1
F[1] = 1

def Fib_Mem(n):
    if F[n] > 0:
        return F[n]
    F[n] = Fib_Mem(n-1) + Fib_Mem(n-2)
    return F[n]

