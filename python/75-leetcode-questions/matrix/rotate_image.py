def rotate_image(matrix):
    if not matrix or not len(matrix):
        return None

    M = len(matrix)
    N = len(matrix[0])

    # Transpose.
    for i in range(M):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print("transposed", matrix)

    # Reverse rows.
    for i in range(M):
        for j in range(N >> 1):
            matrix[i][j], matrix[i][N - j - 1] = matrix[i][N - j - 1], matrix[i][j]

    return matrix


#matrix = [
#        [5, 1, 9, 11],
#        [2, 4, 8, 10],
#        [13, 3, 6, 7],
#        [15, 14, 12, 16]
#        ]

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ]

#matrix = [
#        [1, 2],
#        [3, 4],
#        ]


print("matrix    ", matrix)
print("reversed  ", rotate_image(matrix))
