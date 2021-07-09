class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0

    return max(height(root.left), height(root.right)) + 1


#def is_tree_balanced(root):
#    stack = [(root, 1)]
#    depths = []
#
#    while stack:
#        node, depth = stack.pop()
#
#        if not node.left and not node.right:
#            depths.append(depth)
#
#        if node.left:
#            stack.append((node.left, depth + 1))
#        if node.right:
#            stack.append((node.right, depth + 1))
#
#    return max(depths) - min(depths) > 1


def is_tree_balanced(root):
    if not root:
        return False

    return abs(height(root.left) - height(root.right)) <= 1


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.left.left.left = TreeNode(8)

print(is_tree_balanced(tree))
