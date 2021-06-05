# Iterative
def move(arr, i):
    num = arr[i]
    prev = i - 1

    while i > 0 and num < arr[prev]:
        arr[i], arr[prev] = arr[prev], arr[i]
        i -= 1
        prev -= 1
    arr[i] = num


def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            move(arr, i)
    return arr


arr = [4, 2, 5, 3, 6, 1, 9, 8]
print(insertion_sort(arr))
