# Given an array of distinct integer values, count the number of pairs
# of integers that have difference `k`.

# O(N^2)

# `k` = 2.
def diff_two(arr):
    pairs = set()
    for i, i_item in enumerate(arr):
        for j, j_item in enumerate(arr):
            if j is i:
                continue

            if abs(i_item - j_item) == 2:
                pairs.add(tuple(sorted([i_item, j_item])))

    print(sorted(pairs))


diff_two([1, 7, 5, 9, 2, 12, 3,])
