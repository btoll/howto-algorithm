from Tree import Tree


# Recursive
def path_sum(root, current_sum):
    current_sum -= root.value

    if not root.left and not root.right:
        return current_sum == 0

    if root.left or root.right:
        return path_sum(root.left, current_sum) or path_sum(root.right, current_sum)


# Iterative
def path_sum(root, target_sum):
    stack = [(root, target_sum - root.value)]
    visited = []

    while stack:
        node, current_sum = stack.pop()

        if current_sum == 0 and not node.left and not node.right:
            return True

        if node.right:
            stack.append((node.right, current_sum - node.right.value))

        if node.left:
            stack.append((node.left, current_sum - node.left.value))

    return False


# Construct the tree from the list and print the search order.
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#nodes = [1, 2, 3, 4, 5, 6, 7, 8]
tree = Tree(nodes)
print(path_sum(tree.get_root(), 23))
