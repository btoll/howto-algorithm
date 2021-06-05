def naive(haystack, needle):
    for i in range(0, len(haystack) - len(needle) + 1):
        match = 0
        while haystack[i + match] is needle[match]:
            if match == len(needle) - 1:
                print(f"Match between {i} and {i + match}")
                break
            match += 1


print(naive("bentoll", "ll"))
