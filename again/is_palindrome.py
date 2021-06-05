def is_palindrome(s):
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if j < i:
            return True
        if s[j] != s[i]:
            return False
        i += 1


print(is_palindrome("zbuz"))
