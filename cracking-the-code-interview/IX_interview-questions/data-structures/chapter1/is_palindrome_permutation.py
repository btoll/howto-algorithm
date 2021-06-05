def is_palindrome_permutation(s):
    c = {}
    for char in s:
        if c.get(char):
            c[char] = c.get(char) + 1
        else:
            c[char] = 1

    n = 0
    for v in c.values():
        if n == 1:
            return False
        if v == 1:
            n += 1

    return True

print(is_palindrome_permutation("tactcoa"))
