def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def bubble(a):
    for i in range(len(a)):
        for j in range(1, len(a)):
            if a[j] < a[j - 1]:
                swap(a, j, j - 1)

    return a


print(bubble([8, -1, 4, 5, 1, 9, 7, 3, 0]))
