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

def randPartition(t, l, r):
    s = random.randint(l, r)
    t[s], t[r] = t[r], t[s]
    return partition(t, l, r)

def check(t, sum):
    min = 0
    max = len(t)-1

    while min < max:
        if t[min] + t[max] == sum:
            print(f'YES: (t[{min}] = {t[min]}) + (t[{max}] = {t[max]})\t=\t{sum}')
            return min, max
        elif t[min] + t[max] > sum:
            max -=1
        elif t[min] + t[max] < sum:
            min +=1
    print(f'Error: in array is not 2 elements equal {sum}')


sum = 5
t = [1, 4, 3, 6, 5, 2]
printTab(t)

quickSort(t, 0, len(t)-1)
printTab(t)

check(t, sum)
