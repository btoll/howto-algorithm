def move_zeroes_right(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
    return arr


def move_zeroes_left(arr):
    k = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            arr[k], arr[i] = arr[i], arr[k]
            k -= 1
    return arr


arr = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print(move_zeroes_right(arr))
arr = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print(move_zeroes_left(arr))
