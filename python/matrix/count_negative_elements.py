import ipdb
import numpy


# https://www.techiedelight.com/count-negative-elements-present-sorted-matrix/

list1 = [-7, -3, -1, 3, 5]
list2 = [-3, -2, 2, 4, 6]
list3 = [-1, 1, 3, 5, 8]
list4 = [ 3, 4, 7, 8, 9]


def count(matrix):
    c = 0
    for row in matrix:
        if row[-1] < 0:
            c += len(row)
        else:
            for n in range(len(row) - 2, -1, -1):
                if row[n] < 0:
                    c += 1
    return c


def count(matrix):
    i, j = 0, len(matrix[0]) - 1
    negative = 0
    while i < len(matrix) and j >= 0:
        if matrix[i][j] < 0:
            negative += j + 1
            i += 1
        else:
            j -= 1
    return negative


matrix = numpy.array([list1, list2, list3, list4])
print("negative elements =", count(matrix))
