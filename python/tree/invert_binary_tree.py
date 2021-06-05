from Tree import Tree


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


# Iterative, return list.
def invert(root):
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


# Iterative, return new root.
def invert(root):
    queue = [root]
    while queue:
        node = queue.pop()
        node.right, node.left = node.left, node.right
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)
    return root


# Recursive, return new root.
def invert(root):
    if not root:
        return

    root.right, root.left = root.left, root.right
    invert(root.left)
    invert(root.right)
    return root


nodes = [4, 2, 7, 1, 3, 6, 9]
# Inverted is: [4, 7, 2, 9, 6, 3, 1]
tree = Tree(nodes)
print(bfs(invert(tree.get_root())))
