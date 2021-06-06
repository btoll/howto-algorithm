from Tree import Tree


# Recursive
def preorder(root, visited=[]):
    if not root:
        return

    visited.append(root.value)
    preorder(root.left, visited)
    preorder(root.right, visited)

    return visited


# Iterative
def preorder(root):
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node.value)

        # Note that the order that we push nodes onto the stack is critical.
        # The right node must be pushed on before the left node to maintain
        # the correct order, as the left node will then be popped first.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


tree = Tree([1, 2, 3, 4, 5, 6])
print(preorder(tree.get_root()))
#tree.display()

# [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
