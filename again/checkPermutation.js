const getTotal = s => {
    const t = s.toLowerCase();
    let k = 0;

    for (let i = 0; i < t.length; i++) {
        const ch = ('z'.charCodeAt() - t[i].charCodeAt()) + 1;

        k |= 2 ** ch;
    }

    return k;
}

const checkPermutation = (s, p) => {
    if (s.length !== p.length) {
        return false;
    }

    return getTotal(s) === getTotal(p);
};

console.log(
    checkPermutation('foobar', 'fboaro')
);

