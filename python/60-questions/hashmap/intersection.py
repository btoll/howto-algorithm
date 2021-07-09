def intersection(nums1, nums2):
    if not nums1 or not nums2:
        return

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    c = {}
    for num in nums1:
        c[num] = True

    res = []
    for num in nums2:
        if num in c:
            if c[num]:
                res.append(num)
                c[num] = False

    return res


def intersection(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    intersected = []

    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if nums1[i] not in intersected:
                intersected.append(nums1[i])
            i, j = i + 1, j + 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return intersected


nums1 = [1, 2, 2, 1]
nums1 = [9, 4, 9, 8, 4]
nums2 = [2, 2]
nums2 = [4, 4, 9, 5]
print(intersection(nums1, nums2))
