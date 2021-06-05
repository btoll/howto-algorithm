# Recursive
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# Recursive, memoized
def fibonacci(n):
    c = {}
    def fib(n):
        if n < 2:
            return n

        if not c.get(n):
            c[n] = fib(n - 1) + fib(n - 2)

        return c.get(n)
    return fib(n)


# Iterative, with extra space (list)
def fibonacci(n):
    fib = [0, 1]
    k = n

    while (k):
        fib.append(fib[-2] + fib[-1])
        k -= 1

    return fib[n]


# Iterative, no extra space
def fibonacci(n):
    a = 0
    b = 1

    while n:
        a, b = b, a + b
        n -= 1

    return a


print(fibonacci(5))
