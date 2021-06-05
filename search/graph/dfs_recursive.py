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


traversed = []
visited = ["A"]
def dfs(graph, vertex):
    traversed.append(vertex)
    for neighbor in graph.get(vertex):
        if neighbor not in visited:
            visited.append(neighbor)
            dfs(graph, neighbor)


dfs(adjacency_list, "A")
print(traversed)

# Output:
#["A", "B", "S", "C", "D", "E", "H", "F", "G"]

