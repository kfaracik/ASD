def parrent(i):
    return i//2

def left(i):
    return i*2

def right(i):
    return i*2+1

def size(k):
    return len(k)-1

def size_k(k):                                # funkjca potrzebna do sortowania, uwzględnia zmianę rozmiaru kopca
    return k[0]

def heapify(k, i):                          # O(log(n))
    maks = i
    r = right(i)
    l = left(i)
    if r <= size_k(k) and k[r] > k[maks]:
        maks = r                            # jeśli prawy potomek > parrent to zamień
    if l <= size_k(k) and k[l] > k[maks]:
        maks = l                            # wybieramy największego potomka
    if maks != i:
        k[i], k[maks] = k[maks], k[i]
        #print(k)
        heapify(k, maks)

def buildHeap(k):                           # budowanie kopca O(n)
    for i in range (size(k)//2, 0, -1):
        heapify(k, i)

def heapSort(k):                            # sortowanie kopca rosnąco (odwaracanie) O(log(n))
    buildHeap(k)
    for i in range(size_k(k), 1, -1):
        k[i], k[1] = k[1], k[i]
        k[0] -=1
        heapify(k, 1)
    k[0] = size(k)                                 # aktualizacja rozmiaru kopca
#-----------------------------------------------------------------------------------

def getMax(k):                                     # O(log(n))
    if size_k(k) == 0:
        print("Heap is empty!")
    res = k[1]
    k[1] = k[k[0]]
    k[0] -=1
    heapify(k, 1)
    return res

def getMin(k):
    if size_k(k) == 0:
        print("Heap is empty!")
    heapSort(k)
    res = k[1]
    k[1] = k[k[0]]
    k[0] -= 1
    heapify(k, 1)
    return res

def insert(k, x):
    if size_k(k) == len(k)-1:
        print("No more space in que!")
    k[0] +=1
    k[k[0]] = x
    i = size_k(k)
    while i>=2 and k[i] > k[parrent(i)]:
        k[i], k[parrent(i)] = k[parrent(i)], k[i]
        i = parrent(i)



kk = [10,27,16,13,10,50,9,4,2,3,1]

k = [0,29,23,19,11,7,12,17,3,2,5]           # pierwszy element = size
k[0] = size(k)                              # size = tab[0] = len(tab)-1

#heapSort(k)
print(k)

a = getMax(k)
print(a)
print(k)
print("\n")

insert(k, 31)
print(k)

print(kk)
buildHeap(kk)
print(kk)
