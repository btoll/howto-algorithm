import ipdb


def spiral(n):
    bottom = n
    right = n
    matrix = [[None for _ in range(n)] for _ in range(n)]

    top = 0
    left = 0
    k = 1

    while top < bottom and left < right:
        # top -> right
        for col in range(left, right):
            matrix[top][col] = k
            k += 1
        top += 1

        # right -> bottom
        for row in range(top, bottom):
            matrix[row][right - 1] = k
            k += 1
        right -= 1

        # bottom -> left
        for col in range(right, left, -1):
            matrix[bottom - 1][col - 1] = k
            k += 1
        bottom -= 1

        # left -> top
        for row in range(bottom, top, -1):
            matrix[row - 1][left] = k
            k += 1
        left += 1

    return matrix



print(spiral(3))
