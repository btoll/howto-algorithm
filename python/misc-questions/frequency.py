def frequency(s):
    c = {}

    for i, char in enumerate(s):
        if char in c:
            c[char] += 1
        else:
            c[char] = 1
    return c


print(frequency("abcdeffhabi"))
