/*
const isPermutation = (s1, s2) => {
    if (s1.length !== s2.length) return false;
    return Array.from(s1).sort().join('') === Array.from(s2).sort().join('');
};
*/

/*
const isPermutation = (s1, s2) => {
    if (s1.length !== s2.length) return false;

    let k = 0;
    let l = 0;

    for (let char of s1) {
        k ^= char.codePointAt();
    }

    for (let char of s2) {
        l ^= char.codePointAt();
    }

    return k === l;
};
*/

const isPermutation = (s1, s2) => {
    if (s1.length !== s2.length) return false;

    // Assumption.
    const chars = Array(26).fill(0);

    for (let char of s1) {
        chars[char.charCodeAt() % 26]++;
    }

    for (let char of s2) {
        const val = char.charCodeAt() % 26;
        chars[val]--;
        if (chars[val] < 0) return false;
    }

    return true;
};

const s1 = 'asdfasdfasedf';
const s2 = 'assdfdfasdufa';

console.log(isPermutation(s1, s2));

