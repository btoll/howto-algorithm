import ipdb


# Time complexity is O(nlogn) because of sort.

def merge_intervals(intervals):
    res = [intervals[0]]

    intervals.sort(key = lambda i: i[0])

    for start, end in intervals[1:]:
        prev_end = res[-1][1]

        if start <= prev_end:
            res[-1][1] = max(prev_end, end)
        else:
            res.append([start, end])

    return res


intervals = [[1, 5], [3, 7], [4, 6], [6, 8]]
#intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
print(merge_intervals(intervals))
