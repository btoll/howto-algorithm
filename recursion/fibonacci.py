# Compute the nth Fibonacci number.

c = {}
def fibonacci(n):
    if n < 2:
        return n

    if c.get(n):
        return c.get(n)
    else:
        c[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return c.get(n)


print(fibonacci(10))
