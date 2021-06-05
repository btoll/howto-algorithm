def single_number(nums):
    ret = 0
    for i in nums:
        ret ^= i
    return ret


print(single_number([4, 1, 2, 1, 2]))
