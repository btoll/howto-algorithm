def itob(num):
    bits = []
    while num:
        bits.insert(0, str(num % 2))
        num >>= 1
        if len(bits) % 4 == 0:
            bits.insert(0, " ")
        print("bits", bits)
    return "".join(bits)


print(itob(128))
