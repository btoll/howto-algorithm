adjacency_list = {
    "A" : ["B","S"],
    "B" : ["A"],
    "C" : ["D","E","F","S"],
    "D" : ["C"],
    "E" : ["C","H"],
    "F" : ["C","G"],
    "G" : ["F","S"],
    "H" : ["E"],
    "S" : ["A","C","G"]
}


def dfs(graph, vertex):
    stack = [vertex]
    traversed = []
    visited = [vertex]

    while len(stack):
        vertex = stack.pop()
        traversed.append(vertex)

        for neighbor in reversed(graph.get(vertex, [])):
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)

    return traversed

#def dfs(graph, start_vertex):
#    visited = set()
#    traversal = []
#    stack = [start_vertex]
#    while stack:
#        vertex = stack.pop()
#        if vertex not in visited:
#            visited.add(vertex)
#            traversal.append(vertex)
#            # add vertex in the same order as visited
#            stack.extend(reversed(graph[vertex]))
#    return traversal


print(dfs(adjacency_list, "A"))

# Output:
#["A", "B", "S", "C", "D", "E", "H", "F", "G"]

