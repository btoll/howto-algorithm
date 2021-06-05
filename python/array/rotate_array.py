# Time O(N)
# Space O(N)
def rotate_array(nums, k):
    ret = [None] * len(nums)
    for i in range(len(nums)):
        idx = (i + k) % len(nums)
        ret[idx] = nums[i]
    return ret


# Time O(N * K)
# Space O(1)
def rotate_array(nums, k):
    # Speed up the rotation.
    k %= len(nums)

    for i in range(k):
        previous = nums[-1]
        for j in range(len(nums)):
            print("previous", previous)
            tmp = previous
            previous = nums[j]
            nums[j] = tmp
#            nums[j], previous = previous, nums[j]
        print()
    return nums


def reverse(nums, start, end):
    while start < end:
        nums[end], nums[start] = nums[start], nums[end]
        start, end = start + 1, end - 1


# Reverse array and sub-arrays.
# Time O(N)
# Space O(1)
def rotate_array(nums, k):
    n = len(nums)
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
#nums = [1, 2, 3, 4]
k = 4
print(rotate_array(nums, k))
