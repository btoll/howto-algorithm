import ipdb


def get_neighbors():
    return [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)
            ]


# BFS
def max_area(grid):
    if not grid or not len(grid):
        return 0

    M = len(grid)
    N = len(grid[0])

    islands = []

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                queue = [(i, j)]
                area = 1

                while queue:
                    i, j = queue.pop()
                    grid[i][j] = 0
                    for x, y in get_neighbors():
                        nx = i + x
                        ny = j + y
                        if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 1:
                            area += 1
                            grid[nx][ny] = 0
                            queue.insert(0, (nx, ny))
                islands.append(area)
    return islands


def dfs(grid, i, jj):
    #    if not(0 <= i < len(grid)) or not(0 <= jj < len(grid[0])) or grid[i][jj] == 0:
    if not(0 <= i < len(grid)) and not(0 <= jj < len(grid[0])):
        return 0

    if 0 <= i < len(grid) and 0 <= jj < len(grid[0]) and grid[i][jj] == 1:
        grid[i][jj] = 0

    print("[dfs(grid, i + x, jj + y) + 1 for x, y in get_neighbors()]", [dfs(grid, i + x, jj + y) + 1 for x, y in get_neighbors()])
    return [dfs(grid, i + x, jj + y) + 1 for x, y in get_neighbors()]

    return area


def max_area(grid):
    if not grid or not len(grid):
        return 0

    area = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                ipdb.set_trace()
                area = max(dfs(grid, i, j), area)
    print(area)


def max_area(grid):
    seen = set()
    def area(rr, cc):
        if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])
                and (rr, cc) not in seen and grid[rr][cc]):
            return 0
        seen.add((rr, cc))
        return (1 + area(rr+1, cc) + area(rr-1, cc) +
                area(rr, cc-1) + area(rr, cc+1))

#    return max(area(r, c)
#               for r in range(len(grid))
#               for c in range(len(grid[0])))

    areas = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                areas.append((area(r, c)))
    return max(areas)


grid = [
  [1, 1, 1, 1, 0],
  [1, 1, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

#grid = [
#  [1, 1, 0, 0, 0],
#  [1, 1, 0, 0, 0],
#  [0, 0, 1, 0, 0],
#  [0, 0, 0, 1, 1]
#]

print(max_area(grid))
