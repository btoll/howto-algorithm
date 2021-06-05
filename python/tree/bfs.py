from Tree import Tree


def breadth_first_search(root):
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


# Construct the tree from the list and print the search order.
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tree = Tree(nodes)
print(breadth_first_search(tree.get_root()))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
