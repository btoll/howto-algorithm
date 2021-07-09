def two_sum2(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        summed = nums[l] + nums[r]
        if summed < target:
            l += 1
        elif summed > target:
            r -= 1
        else:
            return [l, r]
    return []


nums = [2, 7, 11, 15]
print(two_sum2(nums, 26))
