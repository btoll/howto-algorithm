def get_neighbors():
    return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
            ]


def shortest_path(grid):
    M = len(grid)
    N = len(grid[0])

    S = (0, 0)
    E = (7, 5)

    queue = [(S, 0)]
    visited = [[False for i in range(N)] for j in range(M)]

    while queue:
        (r, c), distance = queue.pop()

        if (r, c) == E:
            return distance

        for x, y in get_neighbors():
            nx, ny = r + x, c + y
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny]:
                    queue.insert(0, ((nx, ny), distance + 1))
                    visited[nx][ny] = True
    return 0


grid = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

print(shortest_path(grid))
