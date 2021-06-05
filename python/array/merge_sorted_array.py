def merge_sorted_array(nums1, nums2):
    p = 0
    q = 0
    arr = []

    while p < len(nums1) and q < len(nums2):
        if nums1[p] < nums2[q]:
            arr.append(nums1[p])
            p += 1
        else:
            arr.append(nums2[q])
            q += 1

    while p < len(nums1):
        arr.append(nums1[p])
        p += 1

    while q < len(nums2):
        arr.append(nums2[q])
        q += 1

    return arr


#nums1 = [1, 2, 3, 0, 0, 0]
nums1 = [1, 7, 9]
m = 3
nums2 = [2, 3, 6]
n = 3
print(merge_sorted_array(nums1, nums2))
