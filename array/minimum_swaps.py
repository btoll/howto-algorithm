def swap(arr, p, q):
    l = list(arr)
    l[q], l[p] = l[p], l[q]
    return l

def minimum_swaps(size, arr):
    k = 0
    for n in range(1, size):
        if arr[k] > arr[n]:
            arr = swap(arr, k, n)
            k = n

    return arr

arr = [4, 3, 1, 2,]
print(minimum_swaps(len(arr), arr))
