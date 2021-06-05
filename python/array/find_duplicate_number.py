#def find_duplicate_number(arr):
#    for i in range(len(arr)):
#        for j in range(len(arr)):
#            if i != j and arr[i] == arr[j]:
#                return arr[j]


def find_duplicate_number(arr):
    k = 0
    for num in arr:
        if k & (1 << num) > 0:
            return num
        else:
            k |= 1 << num
    return k


arr = [1, 3, 4, 2, 4]
print(find_duplicate_number(arr))
