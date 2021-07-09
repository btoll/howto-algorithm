def move_zeroes(nums):
    # This is the insertion point (will point to the first zero in the list).
    k = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[k], nums[i] = num, nums[k]
            k += 1
    return nums, i, k


nums = [5, 0, 0, 1, 0, 3, 0, 12]
print(move_zeroes(nums))
