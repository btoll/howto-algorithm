import ipdb


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def not_present(a1, a2):
    a1_set = set(a1)
    a2_set = set(a2)

    for num in a1:
        if num not in a2_set:
            print(num)

    for num in a2:
        if num not in a1_set:
            print(num)


a1 = [1, 2, 3, 4, 5]
#a2 = [0, 1, 2, 3, 5]
a2 = [2, 3, 1, 0, 5]
print(not_present(a1, a2))
