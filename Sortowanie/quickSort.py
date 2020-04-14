import random

def printTab(t):
    print("| ", end='')
    for i in range(len(t)):
        print(f'{t[i]} | ', end='')
    print()

def quickSort(t, l, r):
    if l<r:
        #pivot = partition(t, l, r)     # better for truple
        pivot = randPartition(t, l, r)
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

def randPartition(t, l, r):
    s = random.randint(l, r)
    t[s], t[r] = t[r], t[s]
    return partition(t, l, r)

t = [1, 4, 3, 6, 5, 2]
printTab(t)

quickSort(t, 0, len(t)-1)
printTab(t)
