adjacency_list = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}


def bfs(start, end):
    if start == end:
        return True

    root = adjacency_list.get(start)
    visited = [start]
    stack = [root]

    while stack:
        neighbors = stack.pop()

        for neighbor in neighbors:
            if neighbor not in visited:
                if neighbor == end:
                    return True, visited
                else:
                    visited.append(neighbor)
                    stack.append(adjacency_list.get(neighbor))

    return False, visited


print(bfs("5", "4"))
