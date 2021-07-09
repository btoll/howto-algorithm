import ipdb


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Iterative
def level_order_traversal(root):
    queue = [(root, 0)]
    levels = []

    while queue:
        node, level = queue.pop()

        if len(levels) == level:
            levels.append([])

        levels[level].append(node.value)

        if node.left:
            queue.insert(0, (node.left, level + 1))

        if node.right:
            queue.insert(0, (node.right, level + 1))

    return levels


# Recursive
levels = []
def level_order_traversal(root, level=0):
    if not root:
        return

    if len(levels) == level:
        levels.append([])

    levels[level].append(root.value)

    root.left = level_order_traversal(root.left, level + 1)
    root.right = level_order_traversal(root.right, level + 1)

    return levels


#root = [3, 9, 20, None, None, 15, 7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order_traversal(root))
