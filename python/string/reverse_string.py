def reverse_string(s):
    arr = list(s)
    k = len(s) - 1
    for i in range(len(s)):
        if i > k:
            return "".join(arr)
        arr[i], arr[k] = arr[k], arr[i]
        k -= 1


def reverse_string(arr):
    i = 0
    for j in range(len(arr) - 1, -1, -1):
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr


#First Part of the recursion method
#You need to remember that you won’t have just one call, you’ll have several nested calls
#
#Each call: str === "?"        	                  reverseString(str.subst(1))     + str.charAt(0)
#1st call – reverseString("Hello")   will return   reverseString("ello")           + "h"
#2nd call – reverseString("ello")    will return   reverseString("llo")            + "e"
#3rd call – reverseString("llo")     will return   reverseString("lo")             + "l"
#4th call – reverseString("lo")      will return   reverseString("o")              + "l"
#5th call – reverseString("o")       will return   reverseString("")               + "o"
#
#Second part of the recursion method
#The method hits the if condition and the most highly nested call returns immediately
#
#5th call will return reverseString("") + "o" = "o"
#4th call will return reverseString("o") + "l" = "o" + "l"
#3rd call will return reverseString("lo") + "l" = "o" + "l" + "l"
#2nd call will return reverserString("llo") + "e" = "o" + "l" + "l" + "e"
#1st call will return reverserString("ello") + "h" = "o" + "l" + "l" + "e" + "h"
def reverse_string(arr):
    if not arr:
        return ""
    return reverse_string(arr[1:]) + arr[0]


def reverse_string(s):
    if not s:
        return ""
    return s[-1] + reverse_string(s[1:-1]) + s[0]


def reverse_string(arr):
    def recurse(l, r):
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            recurse(l + 1, r - 1)

        return arr
    return recurse(0, len(arr) - 1)


arr = ["h", "e", "l", "l", "o"]
print(reverse_string(arr))
