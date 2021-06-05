import math


def sales_by_match(size, arr):
    socks = {}
    for sock in arr:
        if socks.get(sock):
            socks[sock] = socks.get(sock) + 1
        else:
            socks[sock] = 1

    pairs = 0
    for v in socks.values():
        pairs = pairs + math.floor(v / 2)

    return pairs


socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sales_by_match(len(socks), socks))
