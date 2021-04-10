# Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3
# where a, b, c and d are integers between 1 and 1000.

r = range(1, 1001)
a = 1
b = 1
c = 1
d = 1

m = {}
for c in r:
    for d in r:
        res = c**3 + d**3
        m[res] = [c, d]

#for a in r:
#    for b in r:
#        res = a**3 + b**3
#        c, d = m.get(res)
#        print(a, b, c, d)

for v in m.values():
    a, b = v
    c, d = v
    print(a, b, c, d)
