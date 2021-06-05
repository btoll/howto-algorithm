matrix = [
#    [1, 1, 1, 0, 0, 0,],
#    [0, 1, 0, 0, 0, 0,],
#    [1, 1, 1, 0, 0, 0,],
#    [0, 0, 2, 4, 4, 0,],
#    [0, 0, 0, 2, 0, 0,],
#    [0, 0, 1, 2, 4, 0,],
	[-1, -1, 0, -9, -2, -2],
	[-2, -1, -6, -8, -2, -5],
	[-1, -1, -1, -2, -3, -4],
	[-1, -9, -2, -4, -4, -5],
	[-7, -3, -3, -2, -9, -9],
	[-1, -3, -1, -2, -4, -5]
]

def hourglass_sum(matrix):
    m = len(matrix[0])
    n = len(matrix)

    # Subtract 2 for both rows and columns
    # so it's not overflowing the grid.
#    k = float("-inf")
    values = []
    for i in range(m - 2):
        for j in range(n - 2):
            hourglass = \
                matrix[i][j] + \
                matrix[i][j+1] + \
                matrix[i][j+2] + \
                \
                matrix[i+1][j+1] + \
                \
                matrix[i+2][j] + \
                matrix[i+2][j+1] + \
                matrix[i+2][j+2]
            values.append(hourglass)
#            if hourglass > k:
#                k = hourglass

#    return k
    return max(values)


print(hourglass_sum(matrix))
