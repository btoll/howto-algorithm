import ipdb

from Tree import TreeNode


# Recursive
# Left -> Node -> Right
#def inorder(root, visited=[]):
#    if not root:
#        return
#
#    inorder(root.left, visited)
#    visited.append(root.value)
#    inorder(root.right, visited)
#
#    return visited


# Iterative
# Left -> Node -> Right
#def inorder(root):
#    # Unlike other iterative traversals, we don't start with the root
#    # already in the stack.
#    stack = []
#    current = root
#    visited = []
#
#    while current or stack:
#        # Traverse as far left as we can.
#        while current:
#            stack.append(current)
#            current = current.left
#
#        # Pop the leftmost node.
#        current = stack.pop()
#        visited.append(current.value)
#
#        # Assume there's a right node.  If not, the next left node will
#        # be popped, and then we'll again assume there's a right node.
#        current = current.right
#    return visited


# Morris traversal.
def inorder(root):
    current = root
    res = []

    while current:
        if not current.left:
            res.append(current.value)
            current = current.right
        else:
            pre = current.left
            # Find the inorder predecessor of current.
            # This will be the right-most node of the left subtree.
            while pre.right:
                pre = pre.right
            pre.right = current

            # This is destroying the original tree which is no bueno!
            tmp = current
            current = current.left
            tmp.left = None

    return res


#nodes = [1, 2, 3, 4, 5, 6]
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
