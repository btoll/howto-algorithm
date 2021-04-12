def get_ord_total(s):
    total = 0
    for char in s:
        total += ord(char)
    return total


def find(s, b):
    s_len = len(s)
    b_len = len(b)
    s_ord_total = get_ord_total(s)
    c = []

    for i, char in enumerate(b):
        if char in s and i + s_len <= b_len:
            if s_ord_total == get_ord_total(b[i:i + s_len]):
                c.append(i)

    return c

print(find("ben", "derpbenpubbnejonbejeb"))
