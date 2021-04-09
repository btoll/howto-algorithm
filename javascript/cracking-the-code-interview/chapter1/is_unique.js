/*
const isUnique = s => {
    const chars = Array(128).fill(0);

    for (let c of s) {
        chars[c.codePointAt() % 128]++;
    }

    return chars.every(c => c < 2);
};
*/

/*
const isUnique = s => {
    s = s.split('').sort().join('');

    const len = s.length;

    for (let i = 0; i < len - 1; i++) {
        if (s[i] === s[i + 1]) return false;
    }

    return true;
};
*/

/*
After viewing solutions in book:

1. Return as soon as we see a char for the 2nd time.
2. Return if string length is > 128 (or 256, extended ascii).

O(1) time and space, since you can argue that the loop never iterates through
more than 128 chars or stores more than 128 chars (otherwise, time is O(n)).

If charset isn't fixed, time is O(c) or O(min(c, n)) and space is O(c).
*/

/*
const isUnique = s => {
    if (s.length > 128) return false;

    const chars = Array(128).fill(0);

    for (let c of s) {
        const val = c.codePointAt();
        if (chars[val]) return false;
        chars[val]++;
    }

    return true;
};
*/

/*
Using a bit vector reduces the space usage by a factor of 8.
*/
const isUnique = s => {
    let checker = 0;
    const a = 'a'.charCodeAt();

    for (let i = 0, len = s.length; i < len; i++) {
        const val = s.charCodeAt(i) - a;
        if ((checker & (1 << val)) > 0) return false;
        checker |= (1 << val);
    }

    return true;
};

//const str = 'abcdefghijklmnopqrstuvwxyz';
const str = 'abdefg';

console.log(isUnique(str));

