def left_rotation(arr, left_rot):
    l_arr = len(arr)

    # Create a second array and then fill these slots
    # with the result of the modulo operation.
    b = [-1] * l_arr

    for i, num in enumerate(arr):
        b[((i - left_rot) % l_arr)] = num

    return b

print(left_rotation([1, 2, 3, 4, 5], 4))


def left_rotation2(a, k):
    return a[k:] + a[:k]


print(left_rotation2([1, 2, 3, 4, 5], 4))
