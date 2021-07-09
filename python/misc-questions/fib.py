def fib(n):
    if n < 2:
        return n

    return fib(n - 2) + fib(n - 1)


def fib(n):
    a = 0
    b = 1

    i = 1
    while i < n:
        b, a = a + b, b
        i += 1

    return b

print(fib(10))
