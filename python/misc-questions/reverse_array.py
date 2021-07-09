def reverse_array(arr):
    l = len(arr)
    for i in range(l >> 1):
        arr[i], arr[l - 1 - i] = arr[l - 1 - i], arr[i]
    return arr


print(reverse_array([1, 2, 3, 4, 5, 6, 7, 8, 9]))
