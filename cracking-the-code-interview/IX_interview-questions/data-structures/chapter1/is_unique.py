# With data structure.
def is_unique(s):
    c = {}
    for char in s:
        if c.get(char):
            return False
        else:
            c[char] = True

    return True

print(is_unique("abcdefghij"))


# With a bit vector.
def is_unique2(s):
    # "bit vector"
    bv = 0
    for char in s:
        # Subtract the size of an int of the architecture.
        # This is kludgy but allows all ascii alpha-chars
        # to "fit" in an int.
        bit = ord(char) - 64
        # Check if bit `bit` is set.
        if (bv >> bit) & 1:
            return False
        # Add to bit vector.
        bv |= 1 << bit

    return True


print(is_unique2("abcdefghij"))
