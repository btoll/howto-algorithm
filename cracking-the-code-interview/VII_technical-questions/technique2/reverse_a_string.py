def reverse(s):
    if not len(s):
        return ""

    return reverse(s[1:]) + s[0]

print(reverse("I am just a little foo, don't worry about it!"))
