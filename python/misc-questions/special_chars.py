def special_chars(bits):
    length = len(bits)
    k = 0

    while k < length - 1:
        if bits[k] == 0:
            k += 1
        else:
            k += 2

    return k == length - 1


# If last bit has to be one char then True.

bits = [1, 1, 1, 0]
#bits = [1, 0, 0]
print(special_chars(bits))
