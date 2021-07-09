import ipdb


#def set_matrix_zeroes(matrix):
#    if not matrix or not len(matrix):
#        return []
#
#    M = len(matrix)
#    N = len(matrix[0])
#
#    has_zero = set()
#    for i in range(M):
#        for j in range(N):
#            if matrix[i][j] == 0:
#                has_zero.add((i, j))
#
#    for row, col in has_zero:
#        for i in range(N):
#            matrix[row][i] = 0
#        for j in range(M):
#            matrix[j][col] = 0


def set_matrix_zeroes(matrix):
    if not matrix or not len(matrix):
        return []

    M = len(matrix)
    N = len(matrix[0])

    r, c = set(), set()

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                r.add(i)
                c.add(j)

    for i in range(M):
        for j in range(N):
            if i in r or j in c:
                ipdb.set_trace()
                matrix[i][j] = 0


#matrix = [
#        [1, 1, 1],
#        [1, 0, 1],
#        [1, 1, 1]
#        ]

matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3,  1, 5]
        ]

print("matrix before", matrix)
print(set_matrix_zeroes(matrix))
print("matrix after ", matrix)
