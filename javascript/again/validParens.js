const validParens = s => {
    if (!s.length) {
        return true;
    }

    const stack = [s[0]];

    for (let i = 1; i < s.length; i++) {
    }

    return true;
};

console.log(
    validParens('()[]{}')
);

