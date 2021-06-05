# Iterative (dynamic programming b/c not adding the outside 1s every time)
def pascals_triangle_2(row_index):
    triangle = []

    for i in range(row_index):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle[row_index - 1]


# Recursive
def pascals_triangle_2(row_index):
    pass


def pascals_triangle_2(rowIndex):
	row = [1]
	for i in range(rowIndex):
		for j in range(i, 0, -1):
			row[j] = row[j] + row[j-1]
		row.append(1)
	return row

row_index = 10
print(pascals_triangle_2(row_index))
