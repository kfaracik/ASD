tab = [6,5,3,2,4,1]
print(tab)
step = 0
for i in range(len(tab)):
    j = i
    while tab[j] < tab[j-1] and j > 0:
        tab[j], tab[j-1] = tab[j-1], tab[j]
        j -= 1
        step +=1
        print(tab, step)
print(tab)