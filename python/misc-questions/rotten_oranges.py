import ipdb


def get_neighbors():
    return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
            ]


def dfs(grid, seen, r, c):
    seen[r][c] = True

    for x, y in get_neighbors():
        nx, ny = r + x, c + y

        if (nx >= 0 and ny >= 0 and
                nx < len(grid) and ny < len(grid[0])):
            if grid[nx][ny] == 1:
                grid[nx][ny] = 2
    ipdb.set_trace()


def rotten_oranges(grid):
    if not grid or not len(grid):
        return -1

    M = len(grid)
    N = len(grid[0])

    seen = [[False for _ in range(N)] for _ in range(M)]

    k = 0
    for r in range(M):
        for c in range(N):
            if grid[r][c] == 2 and seen[r][c] == False:
                ipdb.set_trace()
                dfs(grid, seen, r, c)
                k += 1
    return k


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(rotten_oranges(grid))
