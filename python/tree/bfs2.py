from Tree import Tree

levels = []


# This is the same as DFS (or preorder) except for the outputting, which is different.
# For instance, remove all the level stuff and it becomes DFS ordering.
def breadth_first_search(node, level=0):
    if len(levels) == level:
        levels.append([])

    levels[level].append(node.value)

    if node.left:
        breadth_first_search(node.left, level + 1)

    if node.right:
        breadth_first_search(node.right, level + 1)

    return levels


#def breadth_first_search(root):
#    queue = [[root, 0]]
#    levels = []
#
#    while queue:
#        node, level = queue.pop()
#
#        if len(levels) == level:
#            levels.append([])
#
#        levels[level].append(node.value)
#
#        if node.left:
#            queue.insert(0, [node.left, level + 1])
#        if node.right:
#            queue.insert(0, [node.right, level + 1])
#
#    return levels


# Construct the tree from the list and print the search order.
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tree = Tree(nodes)
print(breadth_first_search(tree.get_root()))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
