import random

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

def select(t, l, r, i):         # szukamy i-tego co do wielkości elementu       O(n)    [pesymistyczna O(n^2)]
    if l == r:    return t[l]   # warunek końcowy
    q = randPartition(t, l, r)  # q = element dzielący tab
    k = q - l + 1               # liczba elementów pomiędzy
    if i == k:  return t[q]     # warunek końcowy
    elif i < k: return select(t, l, q-1, i)     # lewa połowa tab
    else:       return select(t, q+1, r, i-k)   # prawa połowa

t = [11, 3, 5, 7, 9, 1, 13, 15, 17]

print(select(t, 0, len(t)-1, 5))