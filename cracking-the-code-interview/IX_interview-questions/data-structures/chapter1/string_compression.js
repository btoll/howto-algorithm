/*
const stringCompression = s => {
    const a = [];
    let max = 0;

    for (let i = 0; i < s.length - 1; i++) {
        let k = 1;
        a.push(s[i]);

        while (s[i] === s[i + 1]) {
            k++;
            i++;
        }

        max = Math.max(max, k);
        a.push(k);
    }

    return max <= 1 ? s : a.join('');
};
*/

// An optimization would be to calculate the number of compressions needed
// before checking if the newly-computed string is less than the original one.
// In these cases, it would save us from doing all the work of compressing a
// new string only to just return the original one.
const countCompression = s => {
    let counter = 0;
    let compressedLength = 0;

    for (let i = 0; i < s.length - 1; i++) {
        counter++;

        if (s[i] !== s[i + 1]) {
            compressedLength += 1 + counter.toString().length;
            counter = 0;
        }
    }

    return compressedLength + 1 + counter.toString().length;
};

const stringCompression = s => {
    const compressedLength = countCompression(s);
    console.log('compressedLength', compressedLength);
    if (compressedLength >= s.length) return s;

    const a = [];

    for (let i = 0; i < s.length - 1; i++) {
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

const s = 'aabcccccaaa'; // a2b1c5a3;

console.log(stringCompression(s));

