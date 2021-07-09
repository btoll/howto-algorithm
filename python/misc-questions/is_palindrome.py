def is_palindrome(s):
    if not s:
        return False

    if len(s) == 1:
        return True

    length = len(s)

    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False

    return True


s = "cookkooc"
print(is_palindrome(s))
