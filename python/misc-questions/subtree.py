import ipdb


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(root, sub_root):
    if not root:
        return False

    stack = [root]

    while stack:
        node = stack.pop()

        if node.value == sub_root.value and is_subtree(node, sub_root):
            return True

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return False


def is_subtree(root, sub_root):
    if not root or not sub_root:
        return root == sub_root

    if root.value != sub_root.value:
        return False

    return is_subtree(root.left, sub_root.left) and is_subtree(root.right, sub_root.right)


root = [3, 4, 5, 1, 2]
t1 = TreeNode(3)
t1.left = TreeNode(4)
t1.left.left = TreeNode(2)
t1.left.right = TreeNode(2)
#t1.left.right.left = TreeNode(0)
t1.right = TreeNode(5)

sub_root = [4, 1, 2]
t2 = TreeNode(4)
t2.left = TreeNode(2)
t2.right = TreeNode(2)

print(dfs(t1, t2))
