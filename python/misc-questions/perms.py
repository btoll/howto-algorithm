def perms(s, path=""):
    if not s:
        print(path)

    for i in range(len(s)):
        perms(s[:i] + s[i + 1:], path + s[i])


s = "abc"
perms(s)
