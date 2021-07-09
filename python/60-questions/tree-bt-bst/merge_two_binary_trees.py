import ipdb


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


# Non-destructive
# Recursive
#def merge_two_binary_trees(root1, root2):
#    if not root1 and not root2:
#        return None
#
#    if not root1:
#        return root2
#
#    if not root2:
#        return root1
#
#    t3 = TreeNode(root1.value + root2.value)
#    t3.left = merge_two_binary_trees(root1.left, root2.left)
#    t3.right = merge_two_binary_trees(root1.right, root2.right)
#
#    return t3


# Destructive
def merge_two_binary_trees(root1, root2):
    if not root1:
        return root2

    if not root2:
        return root1

    root1.value += root2.value
    root1.left = merge_two_binary_trees(root1.left, root2.left)
    root1.right = merge_two_binary_trees(root1.right, root2.right)

    return root1


# Iterative
# This is close:
# [3, 4, 5, None, None, None, None, 5, 4, 7]
#
# Should be:
# [3, 4, 5, 5, 4, 7]
def merge_two_binary_trees(root1, root2):
    root3 = TreeNode(None)
    root = root3
    stack = [(root1, root2, root3)]

    while stack:
        t1, t2, t3 = stack.pop()

        if t1 and t2:
            t3.value = t1.value + t2.value
            t3.left = TreeNode(None)
            t3.right = TreeNode(None)
            stack.append((t1.right, t2.right, t3.right))
            stack.append((t1.left, t2.left, t3.left))
#        elif not t1 and not t2:
#            t3.left = None
#            t3.right = None
        if not t2:
            t3.left = t1
        if not t1:
            t3.right = t2
    return root


def merge_two_binary_trees(root1, root2):
    if not root1:
        return root2

    stack = [(root1, root2)]

    while stack:
        t1, t2 = stack.pop()
        if not t1 or not t2:
            continue

        t1.value += t2.value
        if not t1.left:
            t1.left = t2.left
        else:
            stack.append((t1.left, t2.left))

        if not t1.right:
            t1.right = t2.right
        else:
            stack.append((t1.right, t2.right))
    return root1

#root1 = [1, 3, 2, 5]
#root2 = [2, 1, 3, None, 4, None, 7]

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)
root1.right = TreeNode(2)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)

#root1 = TreeNode(1)
#root2 = TreeNode(1)
#root2.left = TreeNode(2)

root3 = merge_two_binary_trees(root1, root2)
print("root3", root3)
print("bfs", bfs(root3))
