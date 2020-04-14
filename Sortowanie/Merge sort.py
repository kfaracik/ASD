# recursion
temp = None

def MergeSort(t, left, right):
    if left != right:
        mid = (left + right)//2            # mid of list   -   divide list to 2 parts
        MergeSort(t, left, mid)        # list[p, ..., mid]
        MergeSort(t, mid + 1, right)    # list[mid+1, ..., r]
        Merge(t, left, mid, right)         # merging and sorting divided lists

def Merge(arr, left, mid, right):
    global temp
    for i in range(left, right + 1):
        temp[i] = arr[i]

    k, L, R = left, left, mid + 1
    while L <= mid and R <= right:
        if temp[L] <= temp[R]:
            arr[k] = temp[L]
            L += 1
        else:
            arr[k] = temp[R]
            R += 1
        k += 1

    while L <= mid:
        arr[k] = temp[L]
        L += 1
        k += 1

    while R <= right:
        arr[k] = temp[R]
        R += 1
        k += 1


t = [5, 4, 6, 1, 2, 7, 3]
print(t)
temp = [None for _ in range(len(arr))]
MergeSort(t, 0, len(t) - 1)
print(t)