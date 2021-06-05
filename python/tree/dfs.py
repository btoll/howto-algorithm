from Tree import Tree


def depth_first_search(root):
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node.value)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return visited


# Construct the tree from the list and print the search order.
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#nodes = [1, 2, 3, 4, 5, 6, 7, 8]
tree = Tree(nodes)
print(depth_first_search(tree.get_root()))
