def first_unique_char(s):
    res = {}

    for i, char in enumerate(s):
        if char in res:
            res[char] = None
        else:
            res[char] = i

    for value in res.values():
        if value is not None:
            return value

    return -1


def first_unique_char(s):
    res = {}

    for char in s:
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1

    for i, char in enumerate(s):
        if res[char] == 1:
            return i

    return -1


def first_unique_char(s):
    a = ord("a")
    res = [0] * 26

    for char in s:
        res[ord(char) - a] += 1

    for i, char in enumerate(s):
        if res[ord(char) - a] == 1:
            return i

    return -1


s = "loveleetcode"
s = "leetcode"
s = "aabb"
print(first_unique_char(s))
