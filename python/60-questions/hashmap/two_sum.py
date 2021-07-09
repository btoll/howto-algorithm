def move(nums, i):
    num = nums[i]
    prev = i - 1
    while i > 0 and num < nums[prev]:
        nums[i] = nums[prev]
        i, prev = i - 1, prev - 1
    nums[i] = num


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            move(nums, i)
    return nums


def two_sum(nums, target):
    c = {}
    for i, num in enumerate(nums):
        if num in c:
            return [c[num], i]
        else:
            c[target - num] = i


def two_sum(nums, target):
    nums = bubble_sort(nums)
    print("sorted", nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        summed = nums[left] + nums[right]
        if summed == target:
            return [left, right]
        if summed < target:
            left += 1
        else:
            right -= 1


nums = [7, 2, 15, 11]
print(two_sum(nums, 18))
