def reverse(string):
    bits = list(string)
    i = 0
    for j in range(len(bits) - 1, -1, -1):
        if i > j:
            break
        bits[i], bits[j] = bits[j], bits[i]
        i += 1

    return "".join(bits)


def btoi(string):
    n = 0
    i = len(string) - 1
    for j in range(len(string)):
        bit = int(string[j])
        if bit:
            n += 2**i
        i -= 1
    return n


def itob(n):
    s = ""
    while n:
        s += str(n % 2)
        n //= 2
    return reverse(s)


def add_binary(a, b):
    return itob(btoi(a) + btoi(b))



a = "1010"
b = "1011"
a = "11"
b = "1"
print(add_binary(a, b))
