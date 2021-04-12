# Add all ASCII char values of both strings.
def get_total_ord(l):
    total = 0
    for char in l:
        total += ord(char)
    return total


def is_permutation(l, r):
    return get_total_ord(l) == get_total_ord(r)


print(is_permutation("ebn", "neb"))


# Use a cache.
def is_permutation2(l, r):
    c = {}
    for char in l:
        if c.get(char):
            # Add for duplicate chars.
            c[char] = c.get(char) + 1
        else:
            c[char] = 1

    for char in r:
        # Strategy here is to remove if char count is zero
        # and a simple bool() check tells use if the
        # dict is empty and thus a permutation.
        if c.get(char):
            v = c.get(char)
            if v == 1:
                del c[char]
            else:
                c[char] = v - 1
        else:
            return False

    # Empty dict returns False, i.e. bool({}) is False.
    return not bool(c)

print(is_permutation2("necbzn", "nezbcn"))
