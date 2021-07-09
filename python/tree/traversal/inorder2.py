import ipdb

from Tree import TreeNode


def inorder(root, visited=[]):
    if not root:
        return

    inorder(root.left)
    visited.append(root.value)
    inorder(root.right)

    return visited

def inorder(root):
    visited = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        visited.append(current.value)
        current = current.right
    return visited


def inorder(root):
    current = root
    visited = []

    while current:
        if not current.left:
            visited.append(current.value)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right is not current:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                visited.append(current.value)
                current = current.right

    return visited


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(6)

#               1
#             /   \
#            /     \
#           2       3
#          / \       \
#         /   \       \
#        4     5       6
#
#  inorder [4, 2, 5, 1, 3, 6]

print(inorder(root))
