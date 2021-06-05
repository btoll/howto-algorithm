def valid_palindrome(s, t):
    if len(s) != len(t) or not s.isalpha() or not t.isalpha():
        return False

    return sum([ord(n) for _, n in enumerate(s)]) == sum([ord(n) for _, n in enumerate(t)])


def valid_palindrome(s, t):
    if len(s) != len(t) or not s.isalpha() or not t.isalpha():
        return False

    count = [0] * 26
    for i, char in enumerate(s):
        count[ord(char) - ord("a")] += 1
        count[ord(t[i]) - ord("a")] -= 1

    for _, v in enumerate(count):
        if v != 0:
            return False
    return True


#def valid_palindrome(s):
#    i = 0
#    for j in range(len(s) - 1, -1, -1):
#        if i > j:
#            return True
#        if s[i] != s[j]:
#            return False
#        i += 1


s = "anagram"
t = "nagaram"
print(valid_palindrome(s, t))
