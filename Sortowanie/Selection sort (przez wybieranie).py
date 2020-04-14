tab = [6,5,3,2,4,1]
print(tab)

for j in range(len(tab)):
    min = tab[j]

    for i in range(j+1, len(tab)):
        if tab[i] < min:
            min = tab[i]
            el = i
        if i == len(tab) - 1:
            tab[j], tab[el] = tab[el], tab[j]

print(tab)
