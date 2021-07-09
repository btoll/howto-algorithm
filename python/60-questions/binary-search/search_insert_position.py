# Recursive
def search_insert_position(nums, left, right, target):
    if left > right:
        return left

    mid = (left + right) >> 1

    if nums[mid] == target:
        return mid

    if nums[mid] < target:
        return search_insert_position(nums, mid + 1, right, target)
    else:
        return search_insert_position(nums, left, mid - 1, target)


# Iterative
def search_insert_position(nums, left, right, target):
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


nums = [1, 3, 5, 6]
target = 100
print(search_insert_position(nums, 0, len(nums) - 1, target))
