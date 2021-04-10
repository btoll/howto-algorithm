// Improvement: To ignore all non-alpha chars,
// do something like:
//
//      if 'a'.charCodeAt() <= charToCheck <= 'z'.charCodeAt()
//          charToCheck - 'a'.charCodeAt()
//      else
//          return -1
//
// O(n), where `n` is the length of the string.
/*
const isPalindromePerumutation = s => {
    const chars = Array(26).fill(0);

    for (let char of s) {
        if (char === ' ') continue;
        chars[char.charCodeAt() % 26]++;
    }

    let middle = false;

    for (let i = 0; i < chars.length; i++) {
        const count = chars[i] % 2;

        if (count && !middle) middle = true;
        else if (count && middle) return false;
    }

    return true;
};
*/

// Just go through the string once.
// This is an optimization but will have the same runtime as above O(n)
// and could be slower b/c of the extra computations we need to make.
/*
const isPalindromePerumutation = s => {
    const chars = Array(26).fill(0);
    let isOdd = 0;

    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (char === ' ') continue;

        const val = char.charCodeAt() % 26;

        chars[val]++;

        const count = chars[val] % 2;

        if (count) isOdd++;
        else isOdd--;
    }

    return isOdd < 2;
};
*/

const checkChar = char => {
    const a = 'a'.charCodeAt();
    const z = 'z'. charCodeAt();
    const c = char.charCodeAt();

    if (a <= c && c <= z) return c - a;
    else return -1;
};

// Use a bit vector.
const isPalindromePerumutation = s => {
    let bitVector = 0;

    for (let char of s) {
        const val = checkChar(char);

        if (val !== -1) {
            if ((bitVector & (1 << val)) > 0) {
                // Flip the bit back to 0 if the letter has already been seen.
                bitVector ^= (1 << val);
            } else {
                bitVector |= 1 << val;
            }
        }
    }

    // Return `true` if zero (only pairs of letters) or
    // number is a power of two (only one odd letter).
    return bitVector === 0 ||
        (bitVector & (bitVector - 1)) === 0
};

const s = 'tact coa';

console.log(isPalindromePerumutation(s));

