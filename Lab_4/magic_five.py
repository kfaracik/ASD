def printTab(t):
    print("| ", end='')
    for i in range(len(t)):
        print(f'{t[i]} | ', end='')
    print()

def quickSort(t, l, r):
    if l<r:
        pivot = partition(t, l, r)
        quickSort(t, l, pivot - 1)
        quickSort(t, pivot , r)

def partition(t, l, r):
    pivot = t[r]
    i = l - 1

    for j in range(l, r):
        if t[j] <= pivot:       # <= - rising sorted; => - descending sorted
            i +=1
            t[i], t[j] = t[j], t[i]
    t[i+1], t[r] = t[r], t[i+1]
    return i+1

def partition_m5(t, l, r):
    pivot = t[r]
    i = l - 1

    for k in range(l, r):
        if t[k] <= pivot:       # <= - rising sorted; => - descending sorted
            i +=1
            t[i], t[k] = t[k], t[i]
    t[i+1], t[r] = t[r], t[i+1]
    print(t[l+2])
    printTab(t)
    print()
    return t[l+2]

def magic_5(t, l, r, end=False):           # partitnion in common Qs

    if end == True:
        return t[0]

    M5 = [0.0]*(1+len(t)//5)      # array including median of each of the 5 neigbours

    for j in range(0, len(t), 5):
        if j + 4 < len(t):
            #print(f'{j} - {j + 4}')
            quickSort(t, j, j+4)
            M5[j // 5] = t[j+2]
        elif len(t)%2 == 0:     # even rest
            #print(f'{j} - {len(t) - 1} p')
            quickSort(t, j, len(t) - 1)
            delta = int((len(t)-j)/2-1)
            M5[j//5] = (t[j+delta]+t[j+delta+1])/2
        else:                   # odd rest
            #print(f'{j} - {len(t) - 1} np')
            quickSort(t, j, len(t) - 1)
            M5[j//5] = t[j + (len(t) - j)//2]

    #printTab(M5)
    if len(M5) != 1:
        #print("Continue")
        return magic_5(M5, 0, len(M5) - 1)
    else:
        #print("Finito")
        return magic_5(M5, 0, 0, True)


t = [1, 4, 3, 6, 5, 2, 10, 12, 11, 9, 8, 7]

median = magic_5(t, 0, len(t)-1)

print(f' Median: {median}')     # set pivot as median => QS O(n);   UWAGA median możenie nie należeć do elementów tej tab (gdy paż ilość el)




