from Tree import Tree


def postorder(root, nodes):
    if root is None:
        return []

    if root.left:
        postorder(root.left, nodes)
    if root.right:
        postorder(root.right, nodes)
    nodes.append(root.value)

    return nodes


def postorder(root, nodes):
    curr = root
    stack = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        nodes.append(curr.value)
        curr = curr.right

    return nodes


tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(postorder(tree.get_root(), []))

# [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]
