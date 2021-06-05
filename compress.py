s = "aabcccccaaa"

def compress(s):
    count = 0
    arr = []

    for i in range(len(s)):
        count += 1

        if i + 1 >= len(s) or s[i] != s[i + 1]:
            arr.append(s[i])
            arr.append(str(count))
            count = 0

#    count = 1
#    arr = []
#    i = 0
#
#    while i < len(s):
#        arr.append(s[i])
#        while i + count <= len(s) and s[i] == s[i + 1]:
#            count += 1
#            i += 1
#        arr.append(str(count))
#        count = 1
#        i += 1
#
    if len(s) < len(arr):
        return s
    else:
        return "".join(arr)


print(compress(s))
