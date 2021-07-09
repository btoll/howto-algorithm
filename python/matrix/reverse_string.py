def reverse_string(string):
    i = 0
    arr = list(string)
    for j in range(len(arr) - 1, -1, -1):
        if i > j:
            return "".join(arr)
        arr[j], arr[i] = arr[i], arr[j]
        i += 1


def reverse_string(string):
    arr = list(string)
    length = len(arr)
    for i in range(length // 2):
        arr[i], arr[length - 1 - i] = arr[length - 1 - i], arr[i]
    return "".join(arr)


string = "foobar"
print(reverse_string(string))
