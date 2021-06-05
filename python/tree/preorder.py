from Tree import Tree


def preorder(root, nodes):
    if root is None:
        return []

    nodes.append(root.value)
    if root.left:
        preorder(root.left, nodes)
    if root.right:
        preorder(root.right, nodes)

    return nodes


def preorder(root, nodes):
    stack = [root]

    while stack:
        node = stack.pop()

        if node:
            nodes.append(node.value)
            stack.append(node.right)
            stack.append(node.left)

    return nodes


tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(preorder(tree.get_root(), []))
print(tree.display())

# [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
