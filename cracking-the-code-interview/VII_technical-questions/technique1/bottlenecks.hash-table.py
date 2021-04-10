# Given an array of distinct integer values, count the number of pairs
# of integers that have difference `k`.

# O(N)

# `k` = 2.
def diff_two(arr):
    ints = {}
    for item in arr:
        ints[item] = True

    for item in arr:
        if ints.get(item + 2):
            print(item, item + 2)


#diff_two(sorted([1, 7, 5, 9, 2, 12, 3,])
diff_two([1, 7, 5, 9, 2, 12, 3,])
