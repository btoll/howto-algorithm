import ipdb


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Recursive w/ valid range.
def validate_bst(root, low=float("-inf"), high=float("inf")):
    if not root:
        return True

    if not(low <= root.value <= high):
        return False

    return validate_bst(root.left, low, root.value) and validate_bst(root.right, root.value, high)


# Iterative w/ valid range.
def validate_bst(root):
    stack = [(root, float("-inf"), float("inf"))]

    while stack:
        node, low, high = stack.pop()

        if not(low <= node.value <= high):
            return False

        if node.left:
            stack.append((node.left, low, node.value))

        if node.right:
            stack.append((node.right, node.value, high))
    return True


# Iterative
def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


# Iterative, inorder.
def validate_bst(root):
    stack = []
    current = root
    visited = []

    while current or stack:
        # Go left, young man.
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        visited.append(current.value)
        current = current.right
    return is_sorted(visited)


# Recursive, inorder.
def validate_bst(root, visited=[]):
    if not root:
        return visited

    validate_bst(root.left, visited)
    visited.append(root.value)
    validate_bst(root.right, visited)

    return is_sorted(visited)


# Iterative, compare to previous.
def validate_bst(root):
    stack = []
    current = root
    previous = float("-inf")

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if previous > current.value:
            return False

        previous = current.value
        current = current.right
    return True


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(validate_bst(root))
