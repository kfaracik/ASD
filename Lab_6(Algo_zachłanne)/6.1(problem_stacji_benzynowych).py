import random

class Car():
    tankSize = 0
    petrol = 0
    position = 0
    destination = 20

def quickSort(t, l, r, type):
    if l < r:
        border = randPartition(t, l, r, type)
        quickSort(t, l, r - 1, type)
        quickSort(t, l + 1, r, type)

def partition(t, l, r, type):
    pivot = t[r][type]        #randonom
    i = l-1

    for j in range(l, r):
        if t[j][type] < pivot:
            i +=1
            t[i], t[j] = t[j], t[i]

    t[i+1], t[l] = t[l], t[i+1]
    return i+1

def randPartition(t, l, r, type):
    pivot = random.randint(l, r)
    t[pivot], t[r] = t[r], t[pivot]
    return partition(t, l, r, type)

def sortByDistance(t):
    quickSort(t, 0, len(t) - 1, 0)

def sortByPrice(t):
    quickSort(t, 0, len(t) - 1, 1)

def fillPetrol(t, k, i, poz_p, poz_k, combsumbcion):
    delta = t[i][0] - poz_p
    print(f'Poz: {poz_p}')
    print(f'Tankowanie nr:      {k}  w cenie:       {t[i][1]} , km:     {delta}     L:{delta*combsumbcion}')
    return t[i][0], price + delta*combsumbcion*t[i][1]

def printTab(combsumbcion, rang):
    petrolPrice = 5

    for i in range(10, rang+10, 10):
        print(f'[km]:{i}\t[cm^3]:{i*combsumbcion}\t[Zł]:{i*combsumbcion*petrolPrice}')

t = [(0, 4), (20, 4.2), (80, 4.5), (110, 3.9), (170, 3.9), (220, 8)]

sortByPrice(t)
print(t)

poz_p = price = k = 0
poz_k = 20
tank = 70
combsumbcion = 6.3
combsumbcion = combsumbcion/100

while(Car.position <= Car.destination and k<10):
    k +=1
    for i in range(len(t)-1, -1, -1):
        if t[i][0] > poz_p and t[i][0] <= poz_p + tank:
            poz_p, price = fillPetrol(t, k, i, poz_p, poz_k, combsumbcion)
            break

print(f'Koszt podróży: {price}')

printTab(combsumbcion, 1000)