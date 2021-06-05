from Tree import Tree


def binary_tree_level_order_traversal(root):
    levels = []
    queue = [(root, 0)]

    while queue:
        node, level = queue.pop()
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.value)
        if node.left:
            queue.insert(0, (node.left, level + 1))
        if node.right:
            queue.insert(0, (node.right, level + 1))
    return levels


nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tree = Tree(nodes)
print(binary_tree_level_order_traversal(tree.root))
