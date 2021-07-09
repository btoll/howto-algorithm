from Tree import Tree


#def binary_search(arr, l, r, num):
#    if l > r:
#        return -1
#
#    q = (l + r) // 2
#    mid = arr[q]
#    if mid == num:
#        return q
#
#    if mid < num:
#        return binary_search(arr, q + 1, r, num)
#    else:
#        return binary_search(arr, l, q - 1, num)
#
#
#arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#print(binary_search(arr, 0, len(arr) - 1, 1))


# Recursive
def search_in_binary_search_tree(head, value):
    if not head or head.value == value:
        return head

    if head.value > value:
        return search_in_binary_search_tree(head.left, value)
    if head.value < value:
        return search_in_binary_search_tree(head.right, value)


# Iterative
def search_in_binary_search_tree(head, value):
    while head or value != value:
        if head.value > value:
            head = head.left
        else:
            head = head.right
    return head


tree = Tree([4, 2, 7, 1, 3])
print(search_in_binary_search_tree(tree.get_root(), 5))

