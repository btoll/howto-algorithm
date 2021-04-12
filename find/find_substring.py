s = "ben"
s_len = len(s)

b = "derpbenpubenjonbe"
b_len = len(b)

indices = set()
for i, char in enumerate(b):
    if char == s[0] and i + s_le <= b_len:
        for j in range(s_len):
            if s[j] != b[i+j]:
                break
            indices.add(i)

print(sorted(indices))
