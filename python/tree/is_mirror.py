from Tree import Tree


# Recursive
def is_mirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False

    return t1.value == t2.value and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)


# Iterative
def is_mirror(t1, t2):
    queue = [(t1, t2)]

    while queue:
        node1, node2 = queue.pop()
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        if node1.value != node2.value:
            return False

        queue.insert(0, (node1.left, node2.right))
        queue.insert(0, (node2.left, node1.right))


#tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
tree = Tree([1, 2, 2, 3, 4, 4, 3])
print(is_mirror(tree.root.left, tree.root.right))
