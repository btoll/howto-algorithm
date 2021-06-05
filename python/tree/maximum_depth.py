from Tree import Tree


# Bottom up.
def maximum_depth(root):
    if root is None:
        return 0

    return max(maximum_depth(root.left), maximum_depth(root.right)) + 1


# Top down.
ans = 0
def maximum_depth(root, depth=1):
    if root is None:
        return 0
    if not root.left and not root.right:
        return max(ans, depth)

    maximum_depth(root.left, depth + 1)
    maximum_depth(root.right, depth + 1)


# Iterative with a stack.
def maximum_depth(root):
    stack = [(root, 1)]
    depth = 0

    while stack:
        node, current_depth = stack.pop()
        depth = max(current_depth, depth)

        if node.right:
            stack.append((node.right, current_depth + 1))

        if node.left:
            stack.append((node.left, current_depth + 1))

    return depth

tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(maximum_depth(tree.get_root()))

# [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]
