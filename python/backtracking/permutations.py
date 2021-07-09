import ipdb


def backtrack(arr, left, right):
    if left == right:
        print(arr)

    i = left
    while i <= right:
        arr[left], arr[i] = arr[i], arr[left]
        backtrack(arr, left + 1, right)
        arr[left], arr[i] = arr[i], arr[left]
        i += 1


arr = [1, 2, 3]
backtrack(arr, 0, len(arr) - 1)
