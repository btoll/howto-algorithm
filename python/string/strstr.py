def strstr(haystack, needle):
    if not needle:
        return 0

    k = 0
    j = 0

    haystack_len = len(haystack)
    needle_len = len(needle)

    while k < haystack_len:
        while haystack[k] == needle[j]:
            j += 1
            if j == needle_len:
                # Would probably need to do the below operation if finding ALL substrings.
                # k += j
                return k - 1
            k += 1
        k += 1

    return -1


haystack = "hello"
needle = "ll"
#haystack = "aaaaa"
#needle = "bba"
#haystack = ""
#needle = ""
print(strstr(haystack, needle))
