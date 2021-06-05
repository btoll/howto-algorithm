def swap(s, p, q):
    l = list(s)
    l[q], l[p] = l[p], l[q]
    return "".join(l)


def permute(s, l, r):
    if l == r:
        print([s])
        return

    i = l
    while i <= r:
        s = swap(s, l, i)
        permute(s, l + 1, r)
        s = swap(s, l, i)
        i += 1


s = "abc"
permute(s, 0, len(s) - 1)
