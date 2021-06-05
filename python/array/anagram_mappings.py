def anagram_mappings(nums1, nums2):
    if len(nums1) != len(nums2):
        return []

    h2 = {v: [] for v in nums2}
    for i in range(len(nums2)):
        h2[nums2[i]].append(i)

    l = []
    for v in nums1:
        if h2.get(v):
            for n in h2.get(v):
                l.append(n)

    return l

nums1 = [12, 28, 46, 32, 50]
nums1 = [40, 40]
nums2 = [50, 12, 32, 46, 28]
nums2 = [40, 40]

print(anagram_mappings(nums1, nums2))
