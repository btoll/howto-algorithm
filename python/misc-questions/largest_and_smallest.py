def largest_and_smallest(arr):
    smallest = float("inf")
    largest = float("-inf")

    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return smallest, largest


arr = [5, 88, -100, 100, 7, 99]
print(largest_and_smallest(arr))
