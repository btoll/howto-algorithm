def binary_search(array, p, r, item):
    mid = round((p + r) / 2)
    guess = array[mid]

    if p > r:
        return "Not found"

    if guess == item:
        return mid

    if item < guess:
        r = mid - 1
    else:
        p = mid + 1

    return binary_search(array, p, r, item)

array = [-99, -73, -57, -17, 1, 23, 36, 52, 78]
print(binary_search(array, 0, len(array) - 1, 36))
