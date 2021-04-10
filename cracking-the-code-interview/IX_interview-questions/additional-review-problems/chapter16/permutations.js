const permutations = (s, prefix = '') => {
    if (!s.length) console.log(prefix);

    for (let i = 0; i < s.length; i++) {
        // Repeatedly remove the first char.
        const rem = s.slice(0, i) + s.slice(i + 1);

        permutations(rem, prefix + s[i]);
    }
};

console.log(permutations('asdf'));

