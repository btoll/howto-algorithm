const stringCompression = s => {
    const a = [];

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        let n = 1;
        let j = i;

        a[a.length] = ch;

        while (s[++j] === ch) {
            n++;
        }

        a[a.length] = n;

        i = --j;
    }

    const res = a.join('');

    return res.length < s.length ?
        res :
        s;
};

console.log(
    stringCompression('abcccccaaa')
);

