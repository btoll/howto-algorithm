def factorial(n):
    if n == 1:
        return n
    if n < 1:
        return "bad"

    return n * factorial(n - 1)

print(factorial(4))
