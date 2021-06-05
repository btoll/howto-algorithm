from Tree import Tree


def inorder(root, nodes):
    if root is None:
        return []

    if root.left:
        inorder(root.left, nodes)
    nodes.append(root.value)
    if root.right:
        inorder(root.right, nodes)

    return nodes


# Morris traversal.
def inorder(root, nodes):
    curr = root

    while curr:
        if curr.left is None:
            nodes.append(curr.value)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right:
                pre = pre.right
            pre.right = curr
            tmp = curr
            curr = curr.left
            tmp.left = None
    return nodes


def inorder(root, nodes):
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        nodes.append(curr.value)
        curr = curr.right

    return nodes

tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(inorder(tree.get_root(), []))

# [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
