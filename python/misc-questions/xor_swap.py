def xor_swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


print(xor_swap(7, 5))
