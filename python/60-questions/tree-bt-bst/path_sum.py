class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Start at zero and increase to target.
def path_sum(root, target):
    total = 0
    stack = [(root, total)]

    while stack:
        node, total = stack.pop()
        total += node.value

        if total == target:
            return True

        if node.right:
            stack.append((node.right, total))

        if node.left:
            stack.append((node.left, total))

    return False


# Start at target and decrease to zero.
def path_sum(root, target):
    stack = [(root, target - root.value)]

    while stack:
        node, current_total = stack.pop()
        if not node.left and not node.right and current_total == 0:
            return True

        if node.right:
            stack.append((node.right, current_total - node.right.value))

        if node.left:
            stack.append((node.left, current_total - node.left.value))
    return False


# Recursive
def path_sum(root, target):
    if not root:
        return False

    target -= root.value
    if not root.left and not root.right:
        return target == 0

    return path_sum(root.right, target) or path_sum(root.left, target)


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(path_sum(root, 18))
