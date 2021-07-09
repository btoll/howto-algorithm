def bubble_sort(s):
    arr = list(s)

    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return "".join(arr)


def bubble_sort(s):
    arr = list(s)

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return "".join(arr)


def insertion_sort(s):
    arr = list(s)

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            num = arr[i]
            prev = i - 1
            j = i

            while j > 0 and num < arr[prev]:
                arr[j] = arr[prev]
                j, prev = j - 1, prev - 1
            arr[j] = num
    return "".join(arr)


def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = insertion_sort(s1)
    s2 = insertion_sort(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


s1 = "rainnarz"
s2 = "niarniyr"
print(anagrams(s1, s2))
