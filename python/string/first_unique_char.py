# Brute force.
def first_unique_char(string):
    # If there are no unique characters then XORing
    # all chars will return 0.
    x = 0
    for i in range(len(string)):
        x ^= ord(string[i])
    if x == 0:
        return -1

    for i in range(len(string)):
        for j in range(len(string)):
            if i == j:
                continue
            if string[i] == string[j]:
                break
        if j == len(string) - 1:
            return i
    return -1


def first_unique_char(string):
    c = {}
    for i in range(len(string)):
        char = string[i]
        if char in c:
            c[char] += 1
        else:
            c[char] = 1

    for char, value in c.items():
        if value == 1:
            return string.find(char)
    return -1


def first_unique_char(string):
    count = [0] * 26
    n = len(string)

    for i in range(n):
        index = ord(string[i]) - ord("a")
        count[index] += 1

    for i in range(n):
        index = ord(string[i]) - ord("a")
        if count[index] == 1:
            return i


def first_unique_char(s):
    c = {}
    for char in s:
        if char not in c:
            c[char] = 1
        else:
            c[char] += 1

    for i, char in enumerate(s):
        if c.get(char) == 1:
            return i
    return -1


#print(first_unique_char("lloovvee"))
print(first_unique_char("loveleetcode"))
#print(first_unique_char("love"))
