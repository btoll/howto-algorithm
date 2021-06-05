def remove_duplicates():
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


nums = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#nums = [1, 1, 2]
print(remove_duplicates(), nums)
