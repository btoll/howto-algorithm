import ipdb


# For just parenthesis.
def valid_parens(s):
    left = 0
    for char in s:
        if char == "(":
            left += 1
        elif left == 0:
            return False
        else:
            left -= 1
    return left == 0


def valid_parens(s):
    if len(s) < 2:
        return False

    stack = []
    parens = {
        "]": "[",
        "}": "{",
        ")": "("
    }

    for char in s:
        if char not in parens:
            stack.append(char)
        else:
            # If got here and stack is empty that means the
            # string starts invalid!
            if not stack or parens.get(char) != stack.pop():
                return False
    return not stack


# Valid.
s = "()[]{}"
#s = "(((((())))))"
#s = "()()()()"
#s = "((()(())))"

# Invalid.
#s = "([)]"
#s = "(((((((()"
s = ")("

print(valid_parens(s))
