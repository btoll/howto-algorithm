def reverse_string(s):
    arr = list(s)

    i = 0
    for j in range(len(s) - 1, -1, -1):
        if i > j:
            return "".join(arr)
        arr[i], arr[j] = arr[j], arr[i]
        i += 1


def reverse_string(s):
    arr = list(s)
    i = 0
    length = len(s)

    while i < length // 2:
        arr[i], arr[length - 1 - i] = arr[length - 1 - i], arr[i]
        i += 1
    return "".join(arr)


def reverse_string(s):
    if len(s) < 2:
        return s

    return s[-1] + reverse_string(s[1:-1]) + s[0]


def reverse_string(s):
    if len(s) < 2:
        return s

    return reverse_string(s[1:]) + s[0]


print(reverse_string("foobar"))
