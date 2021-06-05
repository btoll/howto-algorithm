def two_sum(arr, target):
    c = {}
    for i in range(len(arr)):
        if target - arr[i] in c:
            return [c.get(target - arr[i]), i]
        else:
            c[arr[i]] = i


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum(nums, target):
    c = {}
    for i in range(len(nums)):
        out = c.get(target - nums[i], None)
        if out is not None:
            return [out, i]
        c[nums[i]] = i


def two_sum(nums, target):
    c = {}
    for i, val in enumerate(nums):
        if val in c:
            return [c[val], i]
        c[target - val] = i


arr = [2, 7, 11, 15]
print(two_sum(arr, 17))
