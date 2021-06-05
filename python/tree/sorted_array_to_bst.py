from random import randint


import ipdb


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sorted_array_to_bst(nodes, left, right):
    if left > right:
        return None

    # Choose left middle node as a root.
    mid = (left + right) // 2
#    # If odd, add 1. Choose right middle node as a root.
#    if (left + right) % 2:
#        mid += 1

    # Choose random middle node as a root.
#    if (left + right) % 2:
#        mid += randint(0, 1)

    root = TreeNode(nodes[mid])
    root.left = sorted_array_to_bst(nodes, left, mid - 1)
    root.right = sorted_array_to_bst(nodes, mid + 1, right)
    return root

nodes = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nodes, 0, len(nodes) - 1)
