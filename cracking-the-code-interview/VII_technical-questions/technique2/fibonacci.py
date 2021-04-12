def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(10)", fibonacci(10))

# Memoized
c = {}

def memoized(n):
    if n < 2:
        return n

    if c.get(n):
        return c.get(n)
    else:
        c[n] = memoized(n - 1) + memoized(n - 2)

    return c[n]

print("memoized(300)", memoized(300))
