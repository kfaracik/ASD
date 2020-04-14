#porównujemy każde dwa a następnie po przejściu całej tablicy zawężamy obszar poszukiwania to przedostatniego

def boubleSort(t):
    size = len(t)
    for i in range(0, size):
        p = 0                            # pozycja
        while p + 1 <= size - i - 1:
            if t[p] > t[p + 1]:
                t[p], t[p + 1] = t[p + 1], t[p]
            p += 1

t = [1,10,9,7,8,5,6,2,4,3]
print(t)
boubleSort(t)
print(t)


