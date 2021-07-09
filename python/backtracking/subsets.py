import ipdb


# https://www.youtube.com/watch?v=REOH22Xwdkk
# Time complexity = O(N * 2^N)

def subsets(nums):
    if not nums:
        return []

    res, subset = [], []

    def dfs(i):
        if i > len(nums) - 1:
            res.append(subset.copy())
            return

        # Decision to include nums[i] (i.e., left node).
        subset.append(nums[i])
        dfs(i + 1)

        # Decision to NOT include nums[i] (i.e., right node).
        subset.pop()
        dfs(i + 1)

        i += 1

    dfs(0)
    return res

nums = [1, 2, 3]
print(subsets(nums))

# [1, 2, 3]
# [2, 3]
# [2]
# [0]
# [0, 1, 2]

# [ [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3] ]
