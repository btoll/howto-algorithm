import ipdb


def get_neighbors():
    return [
            (0, -1), # Top
            (1, 0), # Right
            (0, 1), # Bottom
            (-1, 0), # Left
            ]


def bfs(grid, processed, i, jj):
    queue = [(i, jj)]

    while queue:
        i, jj = queue.pop()
        processed[i][jj] = True
        for x, y in get_neighbors():
            if in_bounds(grid, processed, i + x, jj + y):
                queue.insert(0, (i + x, jj + y))


def create_processed_grid(M, N):
    processed = []
    i = 0
    while i < M:
        row = []
        k = 0
        while k < N:
            row.append(False)
            k += 1
        processed.append(row)
        i += 1
    return processed


def in_bounds(grid, processed, i, j):
    return 0 <= i < len(grid) and \
            0 <= j < len(grid[0]) and \
            grid[i][j] == 1 and \
            not processed[i][j]


# Space O(NM), non-destructive.
def number_of_islands(grid):
    if not grid or not len(grid):
        return 0

#    processed = [[False for i in range(N)] for j in range(M)]
    processed = create_processed_grid(M, N)

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not processed[i][j]:
                islands += 1
                bfs(grid, processed, i, j)
    return islands


# Space O(1), destructrive.
def number_of_islands(grid):
    if not grid or not len(grid):
        return 0

    M = len(grid)
    N = len(grid[0])

    islands = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                islands += 1
                queue = [(i, j)]

                while queue:
                    i, j = queue.pop()
                    grid[i][j] = 0
                    for x, y in get_neighbors():
                        nx = i + x
                        ny = j + y
                        if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 1:
                            queue.insert(0, (nx, ny))
    return islands


def dfs(grid, i, j):
    if not(0 <= i < len(grid)) or not(0 <= j < len(grid[0])) or grid[i][j] == 0:
        return

    grid[i][j] = 0

    for x, y in get_neighbors():
        dfs(grid, i + x, j + y)


# DFS
def number_of_islands(grid):
    if not grid or not len(grid):
        return 0

    islands = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                islands += 1
                dfs(grid, i, j)
    return islands


grid = [
  [1, 1, 1, 1, 0],
  [1, 1, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

grid = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1]
]

print("number of islands =", number_of_islands(grid))
