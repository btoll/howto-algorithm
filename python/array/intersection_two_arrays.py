c = {}
def intersection_two_arrays(nums1, nums2):
    # Optimization, use the smaller list for the hash to save space.
    if len(nums2) > len(nums1):
        nums2, nums1 = nums1, nums2

    for num in nums1:
        if num in c:
            c[num] += 1
        else:
            c[num] = 1

    arr = []
    for num in nums2:
        if num in c and c[num] > 0:
            arr.append(num)
            c[num] -= 1
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            k = i
            num = arr[k]
            prev = k - 1
            while k > 0 and num < arr[prev]:
                arr[k] = arr[prev]
                k, prev = k - 1, prev - 1
            arr[k] = num
    return arr


# https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/
def intersection_two_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    nums1 = insertion_sort(nums1)
    nums2 = insertion_sort(nums2)

    i = 0
    j = 0
    k = 0
    while i < len(nums1):
        if nums1[i] == nums2[j]:
            nums1[k] = nums1[i]
            i += 1
            j += 1
            k += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return nums1[:k]


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

#nums1 = [1, 2, 2, 1]
#nums2 = [2, 2]
print(intersection_two_arrays(nums1, nums2))
