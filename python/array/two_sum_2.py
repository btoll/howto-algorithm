def two_sum(nums, target):
    c = {}
    for i, num in enumerate(nums):
        if target - num in c:
            return [c[target - num], i]
        else:
            c[num] = i


# Sorted (only works on a sorted list).
def two_sum(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        _sum = nums[i] + nums[j]
        if _sum == target:
            return [i, j]
        if _sum > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]


nums = [211, 7, 11, 1]
nums = [2, 7, 11, 15]
print(two_sum(nums, 9))
