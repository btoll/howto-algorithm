import math


def max_array_sum(arr):
    if not len(arr):
        return 0
    if len(arr) < 2:
        return max(arr)

    # key: max index of subarray, value = sum
    dp = {}
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])

    for i, num in enumerate(arr[2:], start = 2):
        dp[i] = max(
                num,
                dp[i - 1],
                dp[i - 2],
                dp[i - 2] + num,
                )

    return dp[len(arr) - 1]


print(max_array_sum([]))
print(max_array_sum([-1]))
print(max_array_sum([1, -1]))
print(max_array_sum([-2, 1, 3, -4, 5]))
print(max_array_sum([3, 7, 4, 6, 5]))
print(max_array_sum([2, 1, 5, 8, 4]))
print(max_array_sum([3, 5, -7, 8, 10]))
print(max_array_sum([-3, -5, -7, -8, -10]))
