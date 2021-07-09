import ipdb
import numpy


def binary_search(matrix, first, last, target):
    if first > last:
        return False

    mid = (first + last) // 2

    first_cell = matrix[mid][0]
    last_cell = matrix[mid][-1]

    if first_cell <= target <= last_cell:
        for num in matrix[mid]:
            if num == target:
                return True
        return False

    if target < first_cell:
        return binary_search(matrix, first, mid - 1, target)
    if last_cell < target:
        return binary_search(matrix, mid + 1, last, target)
    return matrix


# https://icarus.cs.weber.edu/~dab/cs1410/textbook/7.Arrays/row_major.html
def binary_search(matrix, start, end, target):
    if start > end:
        return False

    pivot = (start + end) // 2

#   row * ncols + col
#   ncols = len(matrix[0])

    row = pivot // len(matrix[0])
    col = pivot % len(matrix[0])

    ipdb.set_trace()
    # Below is the same as `pivot`.
    _ = row * len(matrix[0]) + col

    num = matrix[row][col]

    if num == target:
        return True

    if num < target:
        return binary_search(matrix, pivot + 1, end, target)
    else:
        return binary_search(matrix, start, pivot - 1, target)


arrays = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
        ]

matrix = numpy.array(arrays)
#print(binary_search(matrix, 0, len(matrix) - 1, 23))
print(binary_search(matrix, 0, len(matrix) * len(matrix[0]) - 1, 16))
# log(m*n) = log(m) + log(n)

