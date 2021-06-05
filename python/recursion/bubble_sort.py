# Iterative
#def bubble_sort(arr):
#    for i in range(len(arr)):
#        tainted = False
#        for j in range(1, len(arr)):
#            if arr[j] < arr[j - 1]:
#                tainted = True
#                arr[j], arr[j - 1] = arr[j - 1], arr[j]
#        if not tainted:
#            return arr


# Recursive
def bubble_sort(arr, n):
    if n < 2:
        return arr

    # Always need to first bubble up largest list element.
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return bubble_sort(arr, n - 1)


arr = [4, 2, 5, 3, 6, 1, 9, 8]
print(bubble_sort(arr, len(arr)))
#print(bubble_sort(arr))
