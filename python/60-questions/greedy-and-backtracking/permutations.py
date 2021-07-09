import ipdb


# Recursive
def permutations(nums, prefix=[]):
    if not nums:
        print(prefix)

    for i in range(len(nums)):
        remainder = nums[:i] + nums[i + 1:]
        permutations(remainder, prefix + [nums[i]])


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


# Backtracking
def permutations(nums, first=0, res=[]):
    if first == len(nums):
        res.append(nums[:])

    for i in range(first, len(nums)):
        nums[first], nums[i] = nums[i], nums[first]
        permutations(nums, first + 1)
        nums[first], nums[i] = nums[i], nums[first]

    return res


nums = [1, 2, 3]
#nums = [0, 1]
#nums = [1, 2, 3, 4]
print(permutations(nums, 0))
