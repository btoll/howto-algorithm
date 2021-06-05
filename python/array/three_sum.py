# Brute force.
# O(N^3)
def three_sum(nums):
    if len(nums) < 3:
        return []

    res = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                    s = sorted([nums[i], nums[j], nums[k]])
                    if s not in res:
                        res.append(s)
    return res


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def move(nums, i):
    num = nums[i]
    prev = i - 1
    while i > 0 and nums[prev] > num:
        nums[i], nums[prev] = nums[prev], nums[i]
        i, prev = i - 1, prev - 1
    nums[i] = num


def insertion_sort(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            move(nums, i)
    return nums


def two_sum(nums, target):
    nums = insertion_sort(nums)
    low = 0
    high = len(nums) - 1

    while low < high:
        _sum = nums[low] + nums[high]
        if _sum == target:
            return [low, high]
        if _sum < target:
            low += 1
        if _sum > target:
            high -= 1

    return nums


# Approach #1, two pointers.
# O(N^2)
def two_sum2(nums, current, res):
    low = current + 1
    high = len(nums) - 1
    while low < high:
        _sum = nums[current] + nums[low] + nums[high]
        if _sum == 0:
            res.append([nums[current], nums[low], nums[high]])
            low, high = low + 1, high - 1
            while low < high and nums[low] == nums[low - 1]:
                low += 1
        elif _sum < 0:
            low += 1
        else:
            high -= 1


def three_sum(nums):
    nums = insertion_sort(nums)

    res = []
    for i in range(len(nums)):
        # If greater than zero, remaining values cannot sum to zero.
        if nums[i] > 0:
            break
        # Skip over all duplicate values.
        if nums[i] == nums[i - 1]:
            continue
        two_sum2(nums, i, res)
    return res


# Approach #2, hashset.
# O(N^2)
def two_sum(nums, i, res):
    seen = set()
    j = i + 1

    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            res.append([nums[i], nums[j], complement])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


def three_sum(nums):
    nums = insertion_sort(nums)

    res = []
    for i in range(len(nums)):
        # If greater than zero, remaining values cannot sum to zero.
        if nums[i] > 0:
            break
        # Skip over all duplicate values.
        if nums[i] == nums[i - 1]:
            continue
        two_sum(nums, i, res)
    return res


nums = [-1, 0, 1, 2, -1, -4]
# sorted [-4, -1, -1, 0, 1, 2]
#nums = [7, 2, 15, 11]
# sorted [2, 7, 11, 15]
print(three_sum(nums))
