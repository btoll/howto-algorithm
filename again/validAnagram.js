/*
const validAnagram = (s, t) => {
    let sNum = 0;
    let tNum = 0;

    if (s.length !== t.length) {
        return false;
    }

    return s.split('').sort().join('') === t.split('').sort().join('');
};
*/

const validAnagram = (s, t) => {
    if (s.length !== t.length) {
        return false;
    }

    const alpha = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++) {
        alpha[('z'.charCodeAt() - s[i].charCodeAt())]++;
        alpha[('z'.charCodeAt() - t[i].charCodeAt())]--
    }

    return alpha.every(n => n === 0);
};

console.log(
    validAnagram('anagram', 'nagaram')
);

