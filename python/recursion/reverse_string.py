# Iterative
def reverse_string(string):
    i = 0
    arr = list(string)
    for j in range(len(arr) - 1, -1, -1):
        if i > j:
            return "".join(arr)
        arr[j], arr[i] = arr[i], arr[j]
        i += 1


# Iterative
def reverse_string(start, end):
    arr = list(string)
    while start < end:
        arr[end], arr[start] = arr[start], arr[end]
        start, end = start + 1, end - 1
    return "".join(arr)


# Recursive
def reverse_string(string):
    if not string:
        return ""
    return reverse_string(string[1:]) + string[0]


# Recursive
def reverse_string(string):
  if not string:
    return ""
  else:
    return string[-1] + reverse_string(string[:-1])

def reverse_arr(arr, start, end):
    if start > end:
        return arr

    arr[end], arr[start] = arr[start], arr[end]
    return "".join(reverse_arr(arr, start + 1, end - 1))


#def reverse_arr(arr, start, end):
#    if start >= end:
#        return ""
#
#    arr[start], arr[end] = arr[end], arr[start]
#    return reverse_arr(arr, start + 1, end - 1)


string = "benissimo"
#print(reverse_string(0, len(string) - 1))
l = list(string)
print(reverse_arr(l, 0, len(l) - 1))
