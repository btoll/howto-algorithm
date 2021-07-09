class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def min_depth(node):
    if not node:
        return 0
    return min(min_depth(node.left) + 1, min_depth(node.right) + 1)


# DFS
def min_depth(node):
    if not node:
        return 0

    stack = [(root, 1)]
    min_depth = float("inf")

    while stack:
        node, current_depth = stack.pop()

        if not node.left and not node.right:
            min_depth = min(min_depth, current_depth)

        if node.right:
            stack.append((node.right, current_depth + 1))

        if node.left:
            stack.append((node.left, current_depth + 1))

    return min_depth


# BFS
# The drawback of the DFS approach in this case is that all nodes should be visited to ensure that the minimum depth would be found.
# Therefore, this results in a O(N) complexity. One way to optimize the complexity is to use the BFS strategy.
# We iterate the tree level by level, and the first leaf we reach corresponds to the minimum depth.
# As a result, we do not need to iterate all nodes.
def min_depth(node):
    if not node:
        return 0
    queue = [(root, 1)]

    while queue:
        for i in range(len(queue)):
            node, current_depth = queue.pop()
            if not node.left and not node.right:
                return current_depth
            if node.right:
                queue.insert(0, (node.right, current_depth + 1))
            if node.left:
                queue.insert(0, (node.left, current_depth + 1))


#root = [3, 9, 20, null, null, 15, 7]
# 2n + 1
# 2n + 2

#       3
#     /   \
#    /     \
#   9       20
#          / \
#         /   \
#       15     7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

#root = TreeNode(1)
#root.right = TreeNode(2)

#print(bfs(root))
#print(dfs(root))
print(min_depth(root))
