import ipdb

from Tree import TreeNode


# Recursive
def postorder(root, visited=[]):
    if not root:
        return

    ipdb.set_trace()
    postorder(root.left)
    postorder(root.right)
    visited.append(root.value)

    return visited


# Iterative
#def postorder(root):
#    stack = []
#    current = root
#    visited = []
#
#    while current or stack:
#        ipdb.set_trace()
#        while current:
#            stack.append(current)
#            current = current.left
#
#        current = stack.pop()
#
#        while current:
#            stack.append(current)
#            current = current.right
#
#        current = stack.pop()
#        visited.append(current.value)
#        current = current.right
#
#    return visited


# Iterative, a queue and a stack.
#def postorder(root):
#    stack = [root]
#    # `queue` is a queue.
#    queue = []
#
#    while stack:
#        node = stack.pop()
#        queue.insert(0, node.value)
#
#        if node.left:
#            stack.append(node.left)
#        if node.right:
#            stack.append(node.right)
#
#    return queue


#tree = Tree([1, 2, 3, 4, 5, null, 6])
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(6)

print(postorder(root))

#               1
#             /   \
#            /     \
#           2       3
#          / \       \
#         /   \       \
#        4     5       6
#
# postorder [4, 5, 2, 6, 3, 1]
