// Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
//
// For example, given the string "([])[]({})", you should return true.
//
// Given the string "([)]" or "((()", you should return false.

const open = {
    '[': ']',
    '(': ')',
    '{': '}'
};

const close = {
    ']': '[',
    ')': '(',
    '}': '{'
};

const brackets = s => {
    if (close[s[0]]) return false;

    let stack = [];

    for (let char of s) {
        if (open[char]) stack.push(char);
        else if (open[stack.pop()] !== char) return false;
    }

    return stack.length ? false : true;
};

const s = '([])[]({})';
//const s = '([)]';
//const s = '((()';

console.log(brackets(s));

