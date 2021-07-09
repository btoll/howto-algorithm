# Time complexity is O(nlogn) because of sort.

def merge_intervals(intervals):
    res = [intervals[0]]
    k = 0

    intervals.sort(key = lambda i: i[0])

    for i, current in enumerate(intervals, 1):
        prev = res.pop()

        if prev[0] <= current[0] <= prev[1]:
            res.append([prev[0], current[1]])
        else:
            res.append(prev)
            res.append(current)

    return res


intervals = [(1, 5), (3, 7), (4, 6), (6, 8)]
#intervals = [(1, 3), (8, 10), (15, 18), (2, 6)]
print(merge_intervals(intervals))
