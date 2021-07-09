from Tree import Tree


# Recursive
def is_mirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False

    return t1.value == t2.value and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)


# Iterative
def is_mirror(t1, t2):
    queue = [(t1, t2)]

    while queue:
        node1, node2 = queue.pop()
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.value != node2.value:
            return False

        queue.insert(0, (node1.left, node2.right))
        queue.insert(0, (node2.left, node1.right))


#tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
tree = Tree([1, 2, 2, 3, 4, 4, 3])
print(is_mirror(tree.root.left, tree.root.right))
