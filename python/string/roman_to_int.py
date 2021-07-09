roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }

def roman_to_int(s):
    i = 0
    total = 0

    while i < len(s):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total += roman[s[i + 1]] - roman[s[i]]
            i += 2
        else:
            total += roman[s[i]]
            i += 1
    return total


s = "LVIII"
print(roman_to_int(s))
