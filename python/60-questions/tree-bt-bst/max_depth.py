class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    queue = [root]
    visited = []
    while queue:
        node = queue.pop()
        visited.append(node.value)
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)
    return visited


def dfs(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited


def max_depth(node):
    if not node:
        return 0

#    return max(max_depth(node.left) + 1, max_depth(node.right) + 1)
    return max(max_depth(node.left), max_depth(node.right)) + 1


# DFS
def max_depth(root):
    stack = [(root, 1)]
    depth = 0
    while stack:
        node, current_depth = stack.pop()
        if node:
            depth = max(depth, current_depth)
            stack.append((node.left, current_depth + 1))
            stack.append((node.right, current_depth + 1))
    return depth


# BFS
def max_depth(root):
    queue = [root]
    depth = 0
    while queue:
        depth += 1
        for i in range(len(queue)):
            node = queue.pop()
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
    return depth


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
print(max_depth(root))
