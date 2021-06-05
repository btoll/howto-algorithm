def valid_anagram(s, t):
    if len(s) != len(s):
        return False

    a, b = 0, 0

    for i in range(len(s)):
        a += ord(s[i])
        b += ord(t[i])

    return a == b


s = "anagram"
t = "nagaram"
print(valid_anagram(s, t))
