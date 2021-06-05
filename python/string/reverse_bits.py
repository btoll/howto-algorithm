import functools


def reverse_bits(n):
    reverse = []
    while n:
        reverse.append(str(n & 1))
        n >>= 1
    length = len(reverse)
    if length < 32:
        reverse += ["0"] * (32 - length)
    return int("".join(reverse), 2)


def reverse_bits(n):
    ret = 0
    for i in range(32):
        ret <<= 1
        ret |= (n & 1)
        n >>= 1
    return ret


#def reverse_bits(n):
#    ret = 0
#    for shift in range(31, -1, -1):
#        # Get the first bit of n and push it onto reversed, treating it like a queue
#        ret |= (n & 1) << shift
#        n >>= 1
#    return ret

#def reverse_bits(n):
#    ret, power = 0, 24
#    cache = dict()
#    while n:
#        ret += reverse_byte(n & 0xff, cache) << power
#        n = n >> 8
#        power -= 8
#    return ret

#def reverse_byte(byte, cache):
#    if byte not in cache:
#        cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
#    return cache[byte]

def reverse_bits(n):
    ret, power = 0, 24
    while n:
        ret += reverse_byte(n & 0xff) << power
        n = n >> 8
        power -= 8
    return ret

@functools.lru_cache(maxsize=256)
def reverse_byte(byte):
    return (byte * 0x0202020202 & 0x010884422010) % 1023


print(reverse_bits(43261596))
