from Tree import Tree


# Approach 1.
def preorder(node, visited=[]):
    if not node:
        return

    visited.append(node.value)
    preorder(node.left, visited)
    preorder(node.right, visited)
    return visited


def postorder(node, visited=[]):
    if not node:
        return

    postorder(node.left, visited)
    postorder(node.right, visited)
    visited.append(node.value)
    return visited


def is_tree_symmetric(node):
    return preorder(node) == postorder(node)[::-1]


# Approach 2, recursive.
def is_tree_symmetric(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.value == t2.value and is_tree_symmetric(t1.left, t2.right) and is_tree_symmetric(t1.right, t2.left)


# Approach 3, iterative.
def is_tree_symmetric(root):
    queue = [(root, root)]

    while queue:
        t1, t2 = queue.pop()
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.value != t2.value:
            return False
        queue.insert(0, (t1.left, t2.right))
        queue.insert(0, (t1.right, t2.left))
    return True


nodes = [1, 9, 9, 3, 5, 5, 3]
tree = Tree(nodes)
print(is_tree_symmetric(tree.root))
