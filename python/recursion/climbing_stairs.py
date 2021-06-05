#def binary_numbers(n):
#    if n < 2:
#        return n
#
#    return binary_numbers(n - 1) + binary_numbers(n - 1)
#
#
#print(binary_numbers(50))

#def triangular_numbers(n):
#    if n < 2:
#        return n
#
#    return n + triangular_numbers(n - 1)
#
#
#for n in range(20):
#    print(triangular_numbers(n))


# Steps can be one- or two-at-a-time.
def climbing_stairs(n):
    if n < 3:
        return n

    return climbing_stairs(n - 1) + climbing_stairs(n - 2)


def climbing_stairs(i, n):
    if i > n:
        return 0
    if i == n:
        return 1
    return climbing_stairs(i + 1, n) + climbing_stairs(i + 2, n)


def climbing_stairs(n):
    if n == 1:
        return 1

    first = 1
    second = 2

    for i in range(3, n):
        second, first = first + second, second

    return second


print(climbing_stairs(5))
