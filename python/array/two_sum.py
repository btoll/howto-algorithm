def two_sum(arr, target):
    c = {}
    for i in range(len(arr)):
        if target - arr[i] in c:
            return [c.get(target - arr[i]), i]
        else:
            c[arr[i]] = i


# Brute force O(N^2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


#def two_sum(nums, target):
#    c = {}
#    for i in range(len(nums)):
#        out = c.get(target - nums[i], None)
#        if out is not None:
#            return [out, i]
#        c[nums[i]] = i


def two_sum(nums, target):
    c = {}
    for i, val in enumerate(nums):
        if val in c:
            return [c[val], i]
        c[target - val] = i


# O(1) space (only works if sorted).
def two_sum(nums, target):
    nums = sorted(nums)
    i, j = 0, len(nums) - 1

    while i < j:
        _sum = nums[i] + nums[j]
        if _sum == target:
            return [i, j]
        if _sum < target:
            i += 1
        else:
            j -= 1


arr = [2, 7, 11, 15]
arr = [15, 7, 11, 2]
print(two_sum(arr, 9))
