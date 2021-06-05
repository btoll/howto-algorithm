#def get_exponent(n):
#    i = 10
#    while i:
#        if n >= 10**i:
#            return i
#        i -= 1
#    return 1
#
#
#def reverse_integer(n):
#    if 0 <= n < 10:
#        return n
#
#    is_negative = False
#    if n < 0:
#        is_negative = True
#        n *= -1
#
#    i = get_exponent(n)
#    d = 0
#    j = 0
#
#    for exp in range(i, -1, -1):
#        while n >= 10**exp:
#            n -= 10**exp
#            d += 10**j
#        j += 1
#
#    if is_negative:
#        d *= -1
#
#    if -2**31 < d < 2**31 - 1:
#        return d
#    return 0

#def reverse_integer(n, exp):
#    if n == 0:
#        return 0
#
#    if n < 0:
#        is_negative = -1
#        n *= -1
#    else:
#        is_negative = 1
#
#    l = []
#    while n:
#        l.append(str(n % exp))
#        n //= exp
#
#    res = int("".join(l)) * is_negative
#
#    if -2**31 < res < 2**31-1:
#        return res
#    return 0


def reverse_integer(n, exp=10):
    if n < 0:
        is_negative = -1
        n *= -1
    else:
        is_negative = 1

    ret = 0
    while n:
        rem = n % exp
        ret = ret * 10 + rem
        n //= exp

    ret *= is_negative

    if -2**31 <= ret <= 2**31-1:
        return ret
    return 0

#    k = n
#    k *= -1
#
#    ret = 0
#    while k:
#        rem = k % exp
#        ret = ret * 10 + rem
#        k //= exp
#
#    print("ret", ret)
#    if -2**32 <= ret <= 2**31 - 1:
#        if n < 0:
#            return ret * -1
#        else:
#            return ret
#    return 0


#print(reverse_integer(-2147483648, 10))
#print(reverse_integer(-8463847412, 10))
print(reverse_integer(-11, 2))
