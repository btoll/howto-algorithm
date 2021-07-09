# NOTE that the if conditionals before each for loop checks for edge cases
# for when the matrix isn't N x N.

def spiral_matrix(matrix):
    if not matrix or not len(matrix):
        return []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    spiral = []

    while top <= bottom and left <= right:
        # Top -> Right
        if top <= bottom:
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1

        # Right -> Bottom
        if left <= right:
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1

        # Bottom -> Left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                spiral.append(matrix[bottom][col])
            bottom -= 1

        # Left -> Top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                spiral.append(matrix[row][left])
            left += 1

    return spiral


matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

#matrix = [
#        [1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]
#        ]

print(spiral_matrix(matrix))

# 1, 2, 3, 6, 9, 8, 7, 4, 5

