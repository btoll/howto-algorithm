import ipdb


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# BFS, no unique order.
def sorted_array_to_bst(nums, left, right):
    if left > right:
        return

    mid = (left + right) // 2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums, left, mid - 1)
    root.right = sorted_array_to_bst(nums, mid + 1, right)

    return root


nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums, 0, len(nums) - 1)
ipdb.set_trace()
