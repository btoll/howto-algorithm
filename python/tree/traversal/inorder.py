import ipdb

from Tree import Tree


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


# Recursive
# Left -> Node -> Right
def inorder(root, visited=[]):
    if not root:
        return

    inorder(root.left, visited)
    visited.append(root.value)
    inorder(root.right, visited)

    return visited


# Iterative
# Left -> Node -> Right
def inorder(root):
    # Unlike other iterative traversals, we don't start with the root
    # already in the stack.
    stack = []
    current = root
    visited = []

    while current or stack:
        # Traverse as far left as we can.
        while current:
            stack.append(current)
            current = current.left

        # Pop the leftmost node.
        current = stack.pop()
        visited.append(current.value)

        # Assume there's a right node.  If not, the next left node will
        # be popped, and then we'll again assume there's a right node.
        current = current.right
    return visited


nodes = [1, 2, 3, 4, 5, 6]
# preorder [1, 2, 4, 5, 3, 6]
#  inorder [4, 2, 5, 1, 6, 3]
tree = Tree(nodes)
print(inorder(tree.root))
