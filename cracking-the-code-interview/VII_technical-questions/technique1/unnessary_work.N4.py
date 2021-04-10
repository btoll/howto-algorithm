# Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3
# where a, b, c and d are integers between 1 and 1000.

r = range(1, 1001)
a = 1
b = 1
c = 1
d = 1

for a in r:
    for b in r:
        for c in r:
            for d in r:
                if a**3 + b**3 == c**3 + d**3:
                    print(a, b, c, d)
                    break
