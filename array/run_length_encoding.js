const runLengthEncoding = s => {
    const a = [];

    for (let i = 0, len = s.length; i < len; i++) {
        let k = 1;
        a.push(s[i]);

        while (s[i] === s[i + 1]) {
            k++;
            i++;
        }

        a.push(k);
    }

    return a.join('');
};

const runLengthDecoding = s => {
    const a = [];

    /*
    for (let i = 1, len = s.length; i < len; i++) {
        a.push(
            ...Array(
                Number(s[i])
            ).fill(s[i++ - 1])
        );
    }
    */

    for (let i = 0, len = s.length; i < len; i++) {
        const char = s[i++];
        a.push(char);
        let k = 0;

        while (k < Number(s[i]) - 1) {
            a.push(char);
            k++;
        }
    }

    return a.join('');
};

const s = 'aabcccccddd';
console.log(s);
const encoded = runLengthEncoding(s);
console.log(encoded);
console.log(runLengthDecoding(encoded));

