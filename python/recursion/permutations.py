def permutations(head, tail=""):
    if not head:
        perms.append(tail)

    for i in range(len(head)):
        # Remove current character.
#        remainder = head[:i] + head[i+1:]
#        permutations(remainder, tail + head[i])
        permutations(head[:i] + head[i+1:], tail + head[i])

    return perms


perms = []
print(permutations("bean"))
#print(permutations("ben"))
print(len(perms))
