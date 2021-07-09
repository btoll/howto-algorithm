def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def three_sum(nums):
    nums = bubble_sort(nums)

    i = 0
    j = i + 1
    k = len(nums) - 1

    res = []
    while i < len(nums):
        while j < k:
            summed = nums[i] + nums[j] + nums[k]
            if summed < 0:
                j += 1
            elif summed > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
        i += 1
        j = i + 1

    return res

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
# [-4, -1, -1, 0, 1, 2]
