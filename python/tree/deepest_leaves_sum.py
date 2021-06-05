def get_height(root):
    l = len(root)
    i = 0
    while i < 10:
        if (2**i) > l:
            return i
        i += 1


def deepest_leaves_sum(root):
    start = 0
    for i in range(get_height(root) - 1):
        start += 2**i

    count = 0
    for i in range(start, len(root)):
        n = root[i]
        if n is not None:
            count += n

    return count


root = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
print(deepest_leaves_sum(root))
