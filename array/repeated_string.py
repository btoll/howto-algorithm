import collections
import math


def repeated_string(s, n):
    if not s.count("a"):
        return 0

    quotient, remainder = divmod(n, len(s))
    return s.count("a") * quotient + s[:remainder].count("a")
#    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


print(repeated_string("gfcaaaecbg", 547602))
print(repeated_string("aba", 10))
