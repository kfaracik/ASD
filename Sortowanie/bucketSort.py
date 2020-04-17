# zał:
#   - elementy są liczbami z zakresu [0.0  ...  1.0]
#   - rozkład elementów w kubełkach jest równomierny
#   - liczba kubełków jest liniowo zależna od liczby sortowanych elementów        (liczba kubełków = liczba el)   (k = len(tab)

def bucketSort(t, k):   # k = liczba kubełków, względem których posortujemy tab
    b = [[] for i in range(k)]   #tworzymy k kubełków (list)

    for el in t:    b[int(k*el)].append(el) # rozdzielamy elementy do odpowiednich kubełków

    for i in range(k):  b[i].sort()     # sortujemy elementy w każdym kubełku

    res = []
    for i in range(k): res.extend(b[i]) # łączymy kubełki w jedną listę
    return res


t = [0.001, 0.01, 0.056, 0.9, 0.945]

bucketSort(t, len(t))       # liczba kubełków = liczba elementów
print(t)