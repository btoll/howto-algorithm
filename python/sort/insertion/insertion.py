def move(arr, i, k):
    num = arr[i]
    while k > -1:
        if num < arr[k]:
            arr[i] = arr[k]
            i -= 1
            k -= 1
    arr[k] = num


def insertion(arr):
    k = 0
    for i in range(1, len(arr), 1):
        if arr[i] < arr[i - 1]:
            move(arr, i, k)
            k += 1

    return arr


print(insertion([8, -1, 4, 5, 1, 9, 7, 3, 0]))
