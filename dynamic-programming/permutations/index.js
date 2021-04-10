const permutations = (s, prefix = '', arr = []) => {
    if (!s.length) {
        arr.push(prefix);
        return arr;
    }

    for (let i = 0; i < s.length; i++) {
        const rem = s.substr(0, i) + s.substr(i + 1);

        permutations(rem, prefix + s[i], arr);
    }

    return arr;
};

const s = 'abcdefghi';

console.log(permutations(s));

