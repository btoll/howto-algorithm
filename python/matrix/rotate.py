import ipdb


def make_matrix(rows):
    matrix = []
    row = []
    for i in range(1, rows**2 + 1):
        row.append(i)
        if i % rows == 0:
            matrix.append(row)
            row = []
    return matrix


def rotate(matrix):
    if not len(matrix):
        return False
    if len(matrix) != len(matrix[0]):
        return False

    i = 0
    n = len(matrix)
    for layer in range(0, n // 2):
        first = layer
        # Subtract one because `n` is the total number of elements, 1-based.
        last = n - 1 - layer

        i = first
        while i < last:
            offset = i - first

            # Save top.
            top = matrix[first][i]

            # Left -> top.
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> left.
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> bottom.
            matrix[last][last - offset] = matrix[i][last]

            # Top -> right (from saved top).
            matrix[i][last] = top

            i += 1
    return matrix


def rotate(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    length = len(matrix)

    # Transpose the matrix.
    for i in range(length):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Swap the columns.
    # ( To rotate anti-clockwise, swap the rows. )
#    for i in range(length):
#        # This is essentially reversing the row (same could be used for reversing a string).
#        for jj in range(length // 2):
#            matrix[i][jj], matrix[i][length - 1 - jj] = \
#                    matrix[i][length - 1 - jj], matrix[i][jj]

    return matrix


def transpose(matrix):
    length = len(matrix)
    mat = []

    for n in range(length):
        mat.append([matrix[0][n]])

    for row in mat:
        i = 0
        while i < length - 1:
            row.append(row[i] + length)
            i += 1

    return matrix


def transpose(length):
    matrix = []
    for n in range(length):
        row = [n + 1]
        i = 0
        while i < length - 1:
            row.append(row[i] + length)
            i += 1
        matrix.append(row)
    return matrix


def transpose(matrix):
    length = len(matrix)
    for i, row in enumerate(matrix):
        row[0] = i + 1
#        start = i + 1 - length
        for jj in range(1, length):
#            row[jj] = start + length * (i + 1 + jj)
            row[jj] = row[jj - 1] + length
    return matrix


def reverse(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(length // 2):
            matrix[i][j], matrix[i][length - 1 - j] = \
                    matrix[i][length - 1 - j], matrix[i][j]
    return matrix


def rotate(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    matrix = transpose(matrix)

    for i in range(length):
        for jj in range(length // 2):
            matrix[i][jj], matrix[i][length - 1 - jj] = \
                    matrix[i][length - 1 - jj], matrix[i][jj]

    return matrix


def rotate(matrix):
    return reverse(transpose(matrix))


print(rotate(make_matrix(3)))
#print(transpose(make_matrix(3)))
#print(transpose(3))

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
