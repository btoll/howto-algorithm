def move_backward(arr):
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            tmp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = tmp
            print(f"step {i, arr}")
    return arr


def move_forward(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            tmp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = tmp
            print(f"step {i, arr}")
    return arr


def move(arr, i):
    num = arr[i]
    prev = i - 1

    print("num", num)
    print("prev", prev)
    while prev > -1 and num < arr[prev]:
        arr[i] = arr[prev]
        i -= 1
        prev -= 1
    arr[i] = num


def insertion(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            move(arr, i)
    return arr


arr = [10, 3, 7, 1]
#arr = [10, 3]
#print("initial", arr)
#print("end", move_backward(arr))
print(insertion(arr))
