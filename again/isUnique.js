/*
const isUnique = s => {
    const a = [];
    const sl = s.toLowerCase();

    for (let i = 0; i < sl.length; i++) {
        const j = sl[i].charCodeAt() - 'a'.charCodeAt();

        if (a[j] === undefined) {
            a[j] = 1;
        } else {
            return false;
        }
    }

    return true;
};
*/

// Bitmap.
const isUnique = s => {
    if (s.length < 2) {
        return true;
    }

    s = s.toLowerCase();

    let bits = 0;

    for (let i = 0; i < s.length; i++) {
        const j = ('z'.charCodeAt() - s[i].charCodeAt()) + 1;
        const position = 2 ** j;

        if (!(bits & position)) {
            bits |= position;
        } else {
            return false;
        }
    }

    return true;
};

console.log(
    isUnique('abcdefghijklmnob')
);

