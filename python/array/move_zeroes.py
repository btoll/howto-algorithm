# The `i` variable will maintain the current drop index for any
# non-zero elements found by `j`.
#
# Just be sure to increment `i` every time a non-zero item `j`
# is moved to `i`.
#
# `i` will then also serve as the first index will zeroes will
# be back-filled in the array.  Just start at `i` and add zero
# to every slot from there to the end of the array.

#def move_zeroes(nums):
#    i = 0
#    for j in range(len(nums)):
#        if nums[j] != 0:
#            nums[i] = nums[j]
#            i += 1
#
#    for k in range(i, len(nums)):
#        nums[k] = 0
#
#    return nums


def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

nums = [0, 1, 0, 3, 12]
#nums = [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
print(move_zeroes(nums))
